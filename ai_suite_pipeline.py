import pandas as pd
import csv
import json

import aisuite as ai
client = ai.Client()

# load questions in
questions = []
with open('questions.json', 'r') as f:
    questions_data = json.load(f)
    questions = (questions_data['questions'])

# extract questions to run a test
test_questions = [questions[0], questions[10]]

# load the full summary dataframe
df = pd.read_csv('movie_book_dataframe.csv')

# extract synopsis to run a test
test_summaries = df[df['Title'].isin(['Snowpiercer', 'Dracula'])]

# select models
models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]

# initialize list to store the responses
model_results = []

# prepare CSV headers
fieldnames = ['Title', 'Question'] + models

# batch size
batch_size = 10

# pre-generate all message prompts
all_prompts = [
    {
        "title": row['Title'],
        "summary": row['Summary'],
        "question": question,
        "messages": [
            {"role": "system", "content": 
             "You are a story analyzer. Your task is to analyze synopses {with regards to a question} {regarding a statement}. {your answer should be yes or no} {your answer requires you to specify to which degree you agree with the statement}"}, 
            {"role": "user", "content": f"Synopsis: {row['Summary']}, Answer the following question: {question}"}
        ]
    }
    for _, row in test_summaries.iterrows()
    for question in test_questions
]

# Process messages in batches
for i in range(0, len(all_prompts), batch_size):
    batch = all_prompts[i:i + batch_size]

    # Store batch results
    batch_results = []

    for item in batch:
        row_data = {'Title': item['title'], 'Question': item['question']}
        
        # Query each model separately
        for model in models:
            response = client.chat.completions.create(
                model=model,
                messages=item['messages'],
                temperature=0
            )
            row_data[model] = response.choices[0].message.content  # Store response

        batch_results.append(row_data)

    # Store batch results in memory
    model_results.extend(batch_results)

# Write all results to CSV at once
with open('test_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(model_results)

print("CSV file 'test_results.csv' created successfully!")
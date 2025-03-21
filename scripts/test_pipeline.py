import aisuite as ai
client = ai.Client()

models = ["openai:gpt-4o-mini"]

messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    print(response.choices[0].message.content)


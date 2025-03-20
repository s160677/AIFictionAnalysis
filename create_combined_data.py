import csv
import os
import pandas as pd
os.chdir('/Users/seanmcelhenny/Documents/UVA Studies/Masters/7. Thesis/Python files')

# Define the input and output file paths
books_file = 'selected_books.csv'
movies_file = 'selected_movies.csv'
movie_book_dataframe = 'movie_book_dataframe.csv'

# Read the books data
with open(books_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    books_data = list(reader)[1:] # skip header 

# Read the movies data
with open(movies_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    movies_data = list(reader)[1:]  

# Combine the data
combined_data = books_data + movies_data

# Convert to a DataFrame for further editing (average summary = 707 words)
df = pd.DataFrame(combined_data, columns=['Title', 'Summary'])
print(df)

# Write the combined data to a new CSV file
df.to_csv(movie_book_dataframe, index=False)

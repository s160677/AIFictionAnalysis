import pandas as pd
import json
from collections import defaultdict

import os
os.chdir('/Users/seanmcelhenny/Documents/UVA Studies/Masters/7. Thesis/Python files')

# Load the Parquet files and combine them into one DataFrame
df = pd.concat([
    pd.read_parquet('train-00000-of-00001-fac1910a9dbbeb7a.parquet'),
    pd.read_parquet('test-00000-of-00001-fc15cb1e2c3944ab.parquet'),
    pd.read_parquet('validation-00000-of-00001-ef795b97813aa076.parquet')
])

# Drop duplicate titles, keeping only the first occurrence
df = df.drop_duplicates(subset='title')

# Count the unique occurrences in the 'source' column
source_counts = df['source'].value_counts()

 # Count words in each summary
df['Word_Count'] = df['summary'].str.split().str.len()

# Remove summaries longer than 1500 words
df = df[df['Word_Count'] <= 1500]

# Create a CSV file with just the 'title' and 'summary' columns
df[['title', 'summary']].to_csv('selected_books.csv', index=False)

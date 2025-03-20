# Downloading the MovieSUM dataset
from huggingface_hub import InferenceClient
import json
import csv
import os
import pandas as pd
import requests
os.chdir('/Users/seanmcelhenny/Documents/UVA Studies/Masters/7. Thesis/Python files')

# Read the JSONL file into a pandas DataFrame
df = pd.read_json('train.jsonl', lines=True)

# Select only the columns you need
summaries = df[['movie_name', 'imdb_id', 'summary']]

# Split the movie_name column into movie_name and year using regular expression
summaries[['movie_name', 'year']] = summaries['movie_name'].str.extract(r'(.+?)_(\d{4})')

# my tmdb key in order to call API to get genre of each movie 
tmdb_api_key = os.getenv("TMDB_API_KEY")
if not tmdb_api_key:
    raise ValueError("TMDB_API_KEY environment variable not set")

def get_movie_genre(movie_title):
    """Fetches the genre of a movie from TMDb API."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={movie_title.replace(' ', '+')}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            movie_id = data["results"][0]["id"]  # Get the first movie result ID
            
            # Now fetch details including genre
            details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}"
            details_response = requests.get(details_url)
            
            if details_response.status_code == 200:
                details_data = details_response.json()
                genres = [genre["name"] for genre in details_data.get("genres", [])]
                return genres[0] if genres else "Unknown"
    return "Unknown"

# Add a new column for genres in the summaries DataFrame
summaries['genre'] = summaries['movie_name'].apply(get_movie_genre)

print(summaries)

# Select movies ensuring that each genre appears a maximum of 6 times
selected_movies = summaries.groupby('genre').apply(lambda x: x.sample(min(len(x), 6))).reset_index(drop=True)

# Count the number of occurrences of each unique genre
genre_counts = selected_movies['genre'].value_counts()
print(genre_counts)

 # Count words in each summary
selected_movies['Word_Count'] = selected_movies['summary'].str.split().str.len()

# Remove summaries longer than 1500 words
selected_movies = selected_movies[selected_movies['Word_Count'] <= 1500]

# Create a CSV file with just the movie name and summary from selected_movies
selected_movies[['movie_name', 'summary']].to_csv('selected_movies.csv', index=False)



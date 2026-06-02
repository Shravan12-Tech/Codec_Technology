import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("data/tmdb_5000_credits.csv")

# Keep required columns
movies = movies[['movie_id', 'title', 'cast', 'crew']]

# Remove empty values
movies = movies.fillna('')

# Convert cast into vectors
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(movies['cast'])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name):

    movie_name = movie_name.lower()

    movie_index = movies[
        movies['title'].str.lower() == movie_name
    ].index

    if len(movie_index) == 0:
        return ["Movie Not Found"]

    idx = movie_index[0]

    similarity_scores = list(
        enumerate(similarity[idx])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = []

    for movie in similarity_scores[1:6]:

        recommended_movies.append(
            movies.iloc[movie[0]]['title']
        )

    return recommended_movies
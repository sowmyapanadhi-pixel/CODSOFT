import pandas as pd

movies = pd.read_csv("movies.csv")

movie_name = input("Enter a movie name: ")

movie = movies[movies["movie"].str.lower() == movie_name.lower()]

if len(movie) == 0:
    print("Movie not found!")
else:
    genre = movie.iloc[0]["genre"]

    recommendations = movies[
        (movies["genre"] == genre)
        & (movies["movie"].str.lower() != movie_name.lower())
    ]

    print("\nRecommended Movies:")

    for movie in recommendations["movie"]:
        print("-", movie)


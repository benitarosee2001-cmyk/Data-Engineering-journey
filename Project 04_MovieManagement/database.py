import json

from movie import Movie

FILE_NAME = "Movies.json"


def save_movie(movies):

    data = []

    for movie in movies:
        data.append(movie.to_dict())

    with open(FILE_NAME, "w", encoding="utf8") as file:
        json.dump(data, file, indent=4)

    print("Movie saved successfully.")


def load_movie():

    movies = []

    try:

        with open(FILE_NAME, "r", encoding="utf8") as file:
            data = json.load(file)

        for item in data:

            movie = Movie(
                item["ID"],
                item["Title"],
                item["Director"],
                item["Year"],
                item["Rating"]
            )

            movies.append(movie)

        print("Movie loaded successfully.")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("Invalid JSON data.")

    return movies
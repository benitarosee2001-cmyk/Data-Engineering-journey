movie_id = 1000


def generate_id():

    global movie_id

    movie_id += 1

    return movie_id


def update_last_id(movies):

    global movie_id

    if not movies:
        movie_id = 1000
        return

    movie_id = max(movie.id for movie in movies)
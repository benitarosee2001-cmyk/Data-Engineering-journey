from database import load_movie, save_movie
from movie import Movie
from utils import generate_id, update_last_id

movies = load_movie()
update_last_id(movies)


def show_menu():

    print("""
========== Movie Management ==========
1. Add Movie
2. Show Movies
3. Search Movie by ID
4. Edit Movie
5. Delete Movie
6. Count Movies
7. Save Movies
8. Load Movies
9. Statistics
10. Exit
========================================
""")


def add_movie():

    title = input("Title: ")
    director = input("Director: ")

    for movie in movies:
        if movie.title.lower() == title.lower() and movie.director.lower() == director.lower():
            print("Movie already exists.")
            return

    try:

        year = int(input("Year: "))

        if year <= 0:
            print("Invalid Year.")
            return

    except ValueError:
        print("Invalid Input.")
        return

    try:

        rating = float(input("Rating: "))

        if rating < 0 or rating > 10:
            print("Invalid Rating.")
            return

    except ValueError:
        print("Invalid Input.")
        return

    movie_id = generate_id()

    movie = Movie(
        movie_id,
        title,
        director,
        year,
        rating
    )

    movies.append(movie)

    print("Movie added successfully.")


def show_movie():

    if not movies:
        print("No Movies found.")
        return

    for movie in movies:
        movie.show_info()


def search_movie():

    try:

        search_id = int(input("Movie ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for movie in movies:
        if movie.id == search_id:
            movie.show_info()
            return

    print("Movie not found.")


def edit_movie():

    try:

        edit_id = int(input("Movie ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for movie in movies:
        if movie.id == edit_id:

            title = input("Title: ")
            director = input("Director: ")

            try:
            
                year = int(input("Year: "))
            
                if year <= 0:
                    print("Invalid Year.")
                    return
            
            except ValueError:
                print("Invalid Input.")
                return
            
            try:
            
                rating = float(input("Rating: "))
            
                if rating < 0 or rating > 10:
                    print("Invalid Rating.")
                    return
            
            except ValueError:
                print("Invalid Input.")
                return

            movie.update(title, director, year, rating)
            print("Movie updated successfully.")
            return

    print("Movie not found.")


def delete_movie():

    try:

        delete_id = int(input("Movie ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for movie in movies:
        if movie.id == delete_id:
            movies.remove(movie)
            print("Movie deleted successfully.")
            return

    print("Movie not found.")


def count_movie():

    print(f"Total Movies: {len(movies)}")


def statistics():

    if not movies:
        print("No movie found.")
        return

    ratings = [movie.rating for movie in movies]
    highest = max(movies, key=lambda movie:movie.rating)
    lowest = min(movies, key=lambda movie: movie.rating)

    print("\n======= Statistics =======")
    print(f"Total Movie: {len(movies)}")
    print(f"Average Rating: {sum(ratings)/len(ratings)}")
    print(f"Highest Rating: {highest.title} - {highest.rating}")
    print(f"Lowest Rating: {lowest.title} - {lowest.rating}")


def main():

    global movies

    while True:

        show_menu()

        choice = input("Choose: ")

        if choice == "1":
            add_movie()
        
        elif choice == "2":
            show_movie()
        
        elif choice == "3":
            search_movie()
        
        elif choice == "4":
            edit_movie()
        
        elif choice == "5":
            delete_movie()
        
        elif choice == "6":
            count_movie()
        
        elif choice == "7":
            save_movie(movies)
        
        elif choice == "8":
            movies = load_movie()
            update_last_id(movies)
        
        elif choice == "9":
            statistics()
        
        elif choice == "10":
            print("Good Bye.")
            break
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
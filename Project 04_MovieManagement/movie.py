class Movie:

    def __init__(self, movie_id, title, director, year, rating):

        self.id = movie_id
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating


    def show_info(self):

        print(f"""
        ID : {self.id}
        Title : {self.title}
        Director : {self.director}
        Year : {self.year}
        Rating : {self.rating}
        """)


    def update(self, title, director, year, rating):

        self.title = title
        self.director = director
        self.year = year
        self.rating = rating


    def to_dict(self):

        return{
            "ID" : self.id,
            "Title" : self.title,
            "Director" : self.director,
            "Year" : self.year,
            "Rating" : self.rating
        }
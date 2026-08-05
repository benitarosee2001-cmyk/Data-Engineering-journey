class Book:

    def __init__(self, book_id, title, author, pages):

        self.id = book_id
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):

        print(f"""

            Book_id : {self.id}
            Title : {self.title}
            Author : {self.author}
            Pages : {self.pages}

            """)

    def update(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages



    def to_dict(self):

        return{
            "Book_id" : self.id,
            "Title" : self.title,
            "Author" : self.author,
            "Pages" : self.pages
        }
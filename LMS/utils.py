book_id = 1000


def generate_id():

    global book_id

    book_id += 1

    return book_id


def update_last_id(books):

    global book_id

    if not books:
        book_id = 1000
        return

    book_id = max(book.id for book in books)
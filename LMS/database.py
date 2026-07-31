import json

from books import Book

FILE_NAME = "Books.json"

def save_book(books):

    data = []

    for book in books:
        data.append(book.to_dict())

    with open(FILE_NAME, "w", encoding="utf8") as file:
        json.dump(data, file, indent=4)

    print("Book saved successfully.")


def load_book():

    books = []

    try:

        with open(FILE_NAME, "r", encoding="utf8") as file:
            data = json.load(file)

            for item in data:

                book = Book(
                    item["Book_id"],
                    item["Title"],
                    item["Author"],
                    item["Pages"]
                )

                books.append(book)
                print("Book load successfully.")

    except FileNotFoundError:
        print("File not found.")

    except json.JSONDecodeError:
        print("Invalid JSON data.")

    return books
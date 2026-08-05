from books import Book
from database import load_book, save_book
from utils import generate_id, update_last_id

books = load_book()
update_last_id(books)


def show_menu():

    print("\n============ Menu ============")
    print("1.Add Book")
    print("2.Show Books")
    print("3.Search Book by ID")
    print("4.Edit Book")
    print("5.Delete Book")
    print("6.Count Books")
    print("7.Save Book")
    print("8.Load Book")
    print("9.Statistics")
    print("10.Exit")
    print("_" * 90)


def add_book():

    title = input("Title: ")
    author = input("Author: ")

    for book in books:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            print("This book already exists.")
            return

    try:

        pages = int(input("Pages: "))

        if pages <= 0:
            print("Pages must be greater than zero.")
            return

    except ValueError:
        print("Invalid input.")
        return
    

    book_id = generate_id()

    new_book = Book(
                book_id,
                title,
                author,
                pages
            )

    books.append(new_book)

    print(f"Book added successfully. ID = {new_book.id}")


def show_book():

    if not books:
        print("No book found.")
        return

    for book in books:
        book.show_info()


def search_book():

    try:

        search_id = int(input("Book ID: "))

    except ValueError:
            print("Invalid ID.")
            return
    

    for book in books:
        if book.id == search_id:
            book.show_info()
            return

    print("Book not found.")


def edit_book():

    try:

        edit_id = int(input("Book ID: "))

    except ValueError:
            print("Invalid ID.")
            return

    for book in books:
            if book.id == edit_id:

                title = input("Title: ")
                author = input("Author: ")

                try:

                    pages = int(input("Pages: "))

                    if pages <= 0:
                        print("Pages must be greater than zero.")

                except ValueError:
                    print("Invalid pages.")

                books.update(title, author, pages)

            print("Book updated.")
            return

    print("Book not found.")

def delete_book():

    try:

        delete_id = int(input("Book ID: "))

    except ValueError:
            print("Invalid ID.")
            return

    for book in books:
        if book.id == delete_id:
            books.ramove(book)
            print("Book removed successfully.")
            return

    print("Book not found.")


def count_book():

    print(f"Tootal Books: {len(books)}")


def statistics():

    if not books:

        print("No Books found.")
        return

    total_pages = sum(book.pages for book in books)

    average_pages = total_pages / len(books)

    longest_book = max(books, key=lambda book: book.pages)

    shortest_book = min(books, key=lambda book: book.pages)

    print("\n======= Statistics ========")
    print(f"Total Books: {len(books)}")
    print(f"Total Pages: {total_pages}")
    print(f"Average Pages: {average_pages:.2f}")
    print(
        f"Longest Book: "
        f"{longest_book.title} - "
        f"{longest_book.pages} pages"
        )
    print(
        f"Shortest Book: "
        f"{shortest_book.title} - "
        f"{shortest_book.pages} pages"
        )


def main():

    global books

    while True:

        show_menu()

        choice = int(input("Choose: "))

        if choice == "1":
            add_book()

        elif choice == "2":
            show_book()

        elif choice == "3":
            search_book()

        elif choice == "4":
            edit_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            count_book()

        elif choice == "7":
            save_book(books)

        elif choice == "8":
            books = load_book()
            update_last_id(books)

        elif choice == "9":
            statistics()

        elif choice == "10":
            print("Good Bye!")
            break

        else:

            print("Invalid input.")


if __name__ == "__main__":
    main()
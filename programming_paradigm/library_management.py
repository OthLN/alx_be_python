class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"Checked out: {self.title} by {self.author}"
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"Returned: {self.title} by {self.author}"
        else:
            return f"{self.title} is not checked out."

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f"Book '{title}' not found."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"Book '{title}' not found."

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book_title in available_books:
                print(book_title)
        else:
            print("No available books.")

if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    print("\nChecking out '1984':")
    print(library.check_out_book("1984"))
    library.list_available_books()

    print("\nReturning '1984':")
    print(library.return_book("1984"))
    library.list_available_books()

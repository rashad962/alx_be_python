class Book:
    def __init__(self, title, author):
        # Constructor to initialize the book attributes
        self.title = title
        self.author = author

    def __str__(self):
        # String representation for the base class
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        # Initialize the base class (Book) and then the specific attribute for EBook
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # String representation for EBook
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Initialize the base class (Book) and then the specific attribute for PrintBook
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # String representation for PrintBook
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book):
        # Add a Book, EBook, or PrintBook to the library
        self.books.append(book)

    def list_books(self):
        # Print details of each book in the library
        for book in self.books:
            print(book)

# Testing the functionality
if __name__ == "__main__":
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

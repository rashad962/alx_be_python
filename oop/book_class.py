class Book:
    def __init__(self, title, author, year):
        # Constructor to initialize the book attributes
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor to print a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation for informal output (e.g., print)
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation, which is used for recreating the object
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Test the Book class
if __name__ == "__main__":
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

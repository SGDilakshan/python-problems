# Create a class to represent a book with attributes like title, author, and publication year.

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def book_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

# Create book objects
book = Book("Python", "Dilakshan", "2024")
book1 = Book("Java", "Sivanathan", "2025")

# Display info
book.book_info()
print()
book1.book_info()

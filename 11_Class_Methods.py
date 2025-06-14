class Book:
    total_books = 0 

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books added: {cls.total_books}")


book1 = Book("Python Basics")
book2 = Book("Advanced Python")
book3 = Book("Data Structures in Python")

Book.display_total_books()
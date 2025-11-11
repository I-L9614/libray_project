
from core.book import Book

class User:
    count = 1
    def __init__(self, name: str):
        self.name = name
        self.id = User.count
        self.borrowed_books = []
        User.count += 1

    def add_to_borrowed(self, book: Book):
        self.borrowed_books.append(book)

    def remove_from_borrowed(self, book: Book):
        self.borrowed_books.remove(book)



        
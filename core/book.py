import json
class Book:
    
    def __init__(self, title, author, ISBN, is_available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = is_available

    def updet_availabileti(self):
        self.is_available = not self.is_available

    def __str__(self):
        return f"title: {self.title}. author: {self.author}. ISBN: {self.ISBN}. is_available: {self.is_available}."

    def __repr__(self):
        return json.dumps({"title": self.title, "author": self.author, "ISBN": self.ISBN,"is_available": self.is_available})



if __name__ == "__main__":
    book = Book("1984", "George Orvelle", 1234)
    print(book.__dict__)
    print(vars(book))
    print(book)
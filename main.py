
import json
from core.book import Book
from core.library import Library
from core.user import User
import random

if __name__ == "__main__":

    
    with open("data.json" ,"r") as file:
        books_dict = json.load(file)

    print(books_dict)

    library = Library()

    for book in books_dict["books"]:
        library.add_book(
            Book(
                title=book["title"], 
                author=book["author"], 
                ISBN=random.randint(1,1000000)
            )
        )
    
    print(library.books)


    # search
    for book in library.books:
        if book.title == "Pride and Prejudice":
            print(book)
            

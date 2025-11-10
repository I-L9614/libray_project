

class User:
    count = 1
    def __init__(self,name):
        self.name = name
        self.id = User.count
        self.borrowed_books = []
        User.count += 1

    def add_to_borrowed(self,isbn):
        self.borrowed_books.append(isbn)

    def remuv_from_borrowed(self,isbn):
        self.borrowed_books.remove(isbn)



        
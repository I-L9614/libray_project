class Librey(Book,User):
    def __init__(self, list_of_books, list_of_users):
        self.books = list_of_books
        self.users = list_of_users

    
    def add_book(self,Book):
        self.books.append(Book)
        return self.books
    
    







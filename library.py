class Librey(Book,User):
    def __init__(self, list_of_books, list_of_users):
        self.books = list_of_books
        self.users = list_of_users

    
    def add_book(self,Book):
        self.books.append(Book)
        print(f"New book have been aded. book info: {Book}")
        return self.books
    
    def add_user(self, User):
        self.users.append(User)
        print(f"New user registered. user info: {User}")
        return self.users









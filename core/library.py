# from book import Book
# from user import User

class Librey:
    def __init__(self, list_of_books, list_of_users):
        self.books = list_of_books
        self.users = list_of_users
       
    
    def add_book(self,book):
        self.books.append(book)

        
    
    def add_user(self, user):
        self.users.append(user)
        print(f"New user registered. user info: {user}")

    # TODO: use book instance and user instance
    def borow_book(self, user_id, book_id):
        print(f"book:{book_id},has ben borrowed to user: {user_id}")
        
    # TODO: use book instance and user instance
    def return_book(self, user_id, book_id):
        print(f"user: {user_id} has return book: {user_id}")
    
    def list_available_boks(self):
        availabl_books = []
        for i in self.books:
            if i.is_availabl == True:
                availabl_books.append(i)
        return availabl_books
    
    # TODO: Improve
    def look_for_book():
        return input("enter book title")
    
    # TODO: Improve
    def serch_book(self, titel):
        for i in self.books:
            if i.title == titel:
                return i
            else:
                print("book not found")
                continue
    
    # TODO: Improve
    def librery_menu():
        return input("anter choise:\n1.Borow book\n2.return book\n3.add book")
    

    
    




        
        
    










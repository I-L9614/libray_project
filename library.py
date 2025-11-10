from book import *
from user import *

class Librey:
    def __init__(self, list_of_books, list_of_users):
        self.books = list_of_books
        self.users = list_of_users
       
    
    def add_book(self,book):
        self.books.append(book)

        
    
    def add_user(self, user):
        self.users.append(user)
        print(f"New user registered. user info: {user}")

    def borow_book(self, user_id, book_id):
        print(f"book:{book_id},has ben borrowed to user: {user_id}")
        
    
    def return_book(self, user_id, book_id):
        print(f"user: {user_id} has return book: {user_id}")
    
    def list_available_boks(self):
        availabl_books = []
        for i in self.books:
            if i.is_availabl == True:
                availabl_books.append(i)
        return availabl_books
    
    def look_for_book():
        return input("enter book title")
    
    def serch_book(self, titel):
        for i in self.books:
            if i.title == titel:
                return i
            else:
                continue
    
    def librery_menu():
        return input("anter choise:\n1.Borow book\n2.return book\n3.add book")
    

    
    
    




        
        
    










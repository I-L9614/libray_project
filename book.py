class Book:
    
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN  
        
        self.is_available = True

    def apdet_availabileti(self):
        self.is_available = not self.is_available   

    def __str__(self):
        print(f"title: {self.title}.author: {self.author}. ISBN: {self.ISBN}. is_available: {self.is_available}.")


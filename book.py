class Book:
    count = 10000
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.ISBN = Book.count
        Book.count += 2
        self.is_available = True

    def apdet_availabileti(self):
        self.is_available = not self.is_available   

    def __str__(self):
        print(f"title: {self.title}.author: {self.author}. ISBN: {self.ISBN}. is_available: {self.is_available}.")


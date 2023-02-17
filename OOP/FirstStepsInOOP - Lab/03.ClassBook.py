class Book:
    def __init__(self, name , author, pages):
        self.name = name
        self.author = author
        self.pages = pages

book = Book("Indx", "Dani", 200)
print(book.name)
from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # [12, 'Peter']
        self.books_available = {}  # {authors: [books_available]}
        self.rented_books = {}  # {usernames: {book names: days to return}}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books:
                self.rented_books[author][book_name] = days_to_return
            else:
                self.rented_books[author] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user, date in self.rented_books.items():
            if book_name in date:
                return f"The book \"{book_name}\" is already rented and will be available in {date[book_name]} days!"

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]

        else:
            return f"{self.username} doesn't have this book in his/her records!"







# dic = {"Dani": {"Book": 12}}
# del dic["Dani"]["Book"]
# print(dic)
from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {book_name: days_to_return}
            else:
                self.rented_books[book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for k in self.rented_books.keys():
            if book_name in self.rented_books[k]:
                for v in self.rented_books[k].values():
                    return f"The book \"{book_name}\" is already rented and will" \
                           f" be available in {v} days!"

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username]
            self.rented_books[user.username] = {}
            return

        return f"{user.username} doesn't have this book in his/her records!"

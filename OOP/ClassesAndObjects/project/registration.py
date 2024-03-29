from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
            return

        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            return

        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):
        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username != new_username:
            if user.username in library.rented_books:
                name_of_the_book = library.rented_books[user.username].keys()
                days = library.rented_books[user.username].values()
                del library.rented_books[user.username]
                library.rented_books[new_username] = {name_of_the_book: days}

            user.username = new_username
            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return "Please check again the provided username - it should be different than the username used so far!"

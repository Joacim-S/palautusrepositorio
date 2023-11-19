from entities.user import User
import re
import string

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if not re.match('^[a-z]+$', username):
            raise UserInputError('Only a-z allowed in the username')

        if not re.match('^[a-z]{3,}$', username):
            raise UserInputError('Username too short')

        if not len(password) > 7:
            raise UserInputError('Password too short')

        if re.match('^[a-zA-Z]+$', password):
            raise UserInputError("Password can't only contain letters")
            
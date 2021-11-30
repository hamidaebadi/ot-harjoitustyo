from repositories.user_repository import user_repository

class LoginServices:
    def __init__(self):
        self._user_login = user_repository

    def login(self, username, password):
        user_verified = self._user_login.verify_user(username, password)
        return user_verified
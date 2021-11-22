from model.user_model import User
class LoginServices:
    def __init__(self):
        self._user_login = User()

    def login(self, username, password):
        user_verified = self._user_login.verify_user(username, password)
        return user_verified
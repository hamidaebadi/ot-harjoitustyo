from repositories.user_repository import user_repository

class LoginServices:
    """LoginServices class takes control over login operation
    
    Attributes:
        _user_login: object of class UserRepository, give access to database operation
    """

    def __init__(self):
        """Constructore creating new login object

        Attributes:
            _user_login: object of class UserRepository giving access to database
        """
        self._user_login = user_repository


    def login(self, username, password):
        """verify identified user by give username and password

        Args:
            username (str): user's username
            password (str): user's password

        Returns:
            bool: True, if creadentials are correct, otherwise False
        """
        user_verified = self._user_login.verify_user(username, password)
        return user_verified
from database_connection import get_database_connection

class UserRepository:
    """class UserRepository interacting with table users in the database
    """
    def __init__(self, connection):
        """class initializer creating an instance of this class

        Args:
            connection: connection to database
        """
        self._db_connection = connection

    def verify_user(self, username, password):
        """Identifying user by provided credentials

        Args:
            username : user's username
            password : user's password

        Returns: True if user verified, otherwise False
        """
        cursor = self._db_connection.cursor()
        query = " SELECT COUNT(*) FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result[0] == 0:
            return False
        return True

user_repository = UserRepository(get_database_connection())

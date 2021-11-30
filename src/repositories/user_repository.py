from database_connection import get_database_connection
class UserRepository:
    def __init__(self, connection):
        self._db_connection = connection

    def verify_user(self, username, password):
        cursor = self._db_connection.cursor()
        query = " SELECT COUNT(*) FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result[0] == 0:
            return False
        return True



user_repository = UserRepository(get_database_connection())
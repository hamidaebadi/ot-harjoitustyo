from database_connection import get_database_connection
class User:
    def __init__(self):
        self._username = None
        self._full_name = None
        self._db_connection = get_database_connection()

    def verify_user(self, username, password):
        cursor = self._db_connection.cursor()
        query = " SELECT COUNT(*) FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result[0] == 0:
            return False
        return True
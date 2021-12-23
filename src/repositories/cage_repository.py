from initialize_database import get_database_connection
from model.cage_model import Cage


def get_cage_by_row(row):
    return Cage(row['cage_name'], row['cage_capacity'])

class CageRepository:
    """Class CageRepository interact with table Cages in database.
    This class manipulate the state of cages within the program such as
    getting all available cages and adding new cages to the database.

    """
    def __init__(self, connection):
        """Class initializer which creates a new instance of type CageRepository.
        """
        self._db_connection = connection

    def get_cages(self):
        """get all available cages from databas.

        Returns:
            List: on success returns a list of all cages as cage object.
        """
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT * FROM cages;")
        rows = cursor.fetchall()
        cursor.close()
        return list(map(get_cage_by_row, rows))

    def insert_new_category(self, name):
        """Add new cage to the database

        Args:
            name (str): cage's name

        Returns:
            bool: on success returns True, otherwise returns False
        """
        cursor = self._db_connection.cursor()
        row_count = cursor.execute("INSERT INTO cages VALUES (?, 1000)", (name, ))
        self._db_connection.commit()
        if row_count.rowcount == 0:
            return False
        return True
cage_repository = CageRepository(get_database_connection())

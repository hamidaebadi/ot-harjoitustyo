from initialize_database import get_database_connection
from model.cage_model import Cage


def get_cage_by_row(row):
    return Cage(row['cage_name'], row['cage_capacity'])

class CageRepository:
    def __init__(self, connection):
        self._db_connection = connection

    def get_cages(self):
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT * FROM cages;")
        rows = cursor.fetchall()
        cursor.close()
        return list(map(get_cage_by_row, rows))

    
cage_repository = CageRepository(get_database_connection())
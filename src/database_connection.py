import os
import sqlite3
from config import DATABASENAME

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", DATABASENAME))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection

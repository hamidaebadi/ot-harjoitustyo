from config import DATABASENAME
import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", DATABASENAME))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
    drop table if exists users;
    ''')

    connection.commit()

def create_user_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE users(
        first_name CHAR(200) NOT NULL,
        last_name CHAR(200) NOT NULL,
        username CHAR(255) NOT NULL UNIQUE PRIMARY KEY,
        password CHAR(500) NOT NULL
    );
    ''')

    connection.commit()

def add_test_user(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        INSERT INTO users (first_name, last_name, username, password)
        VALUES('test user', 'test1', 'adminTest', '1234');
        '''
    )

    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_user_table(connection)
    add_test_user(connection)


if __name__ == "__main__":
    initialize_database()
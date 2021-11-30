from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS cages")
    cursor.execute("DROP TABLE IF EXISTS products")

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


def create_cages_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE cages(cage_name TEXT UNIQUE PRIMARY KEY, cage_capacity INTEGER);
        '''
    )

    connection.commit()

def add_cages(connection):
    cages = [
        ("Puhelimet", 3000),
        ("kodinkoneet", 5000),
        ("Tietokoneet", 1500),
        ("Pienkoneet", 1000),
        ("Pelit ja viihde", 1000)
    ]
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO cages VALUES (?, ?)", cages)
    connection.commit()


def create_products_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE products (
        product_name TEXT PRIMARY KEY,
        product_category TEXT,
        product_QR TEXT,
        product_quantity INTEGER);
        '''
    )

def insert_into_product(connection):
    items = [
        ("Notebook X", "Puhelimet", "412321", "100"),
        ("Surface 12", "Puhelimet", "4254", "100"),
        ("Galaxy S 10", "Puhelimet", "3242", "10")
        ]
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", items)

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_user_table(connection)
    add_test_user(connection)
    create_cages_table(connection)
    add_cages(connection)
    create_products_table(connection)
    insert_into_product(connection)



if __name__ == "__main__":
    initialize_database()
    
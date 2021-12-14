from initialize_database import get_database_connection

class Cage:
    """class Cage modeling real world cages

    Attributes:
        cage_name: name of the cages in warehouse
        cage_capacity: amount of item could be inserted in a cage
    """
    def __init__(self, cage_name, cage_capacity):
        self.cage_name = cage_name
        self.cage_capacity = cage_capacity



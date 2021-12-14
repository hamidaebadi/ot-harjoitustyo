class User:
    """
    Class User defines user object

    Attributes:
        username: string, user identified by this username
        password: string, user's credentials verified by password
        full_name: string, each user has a fullname
    """
    def __init__(self, username, password, fullname):
        self.username = username
        self.password = password
        self.full_name = fullname


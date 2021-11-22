import unittest
from services.login_services import LoginServices

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.loginSession = LoginServices()
    
    def test_login_successfull_with_correct_account(self):
        account = self.loginSession.login("adminTest", "1234")
        self.assertEqual(account, True)

    def test_login_fail_wrong_crenetials(self):
        account = self.loginSession.login("wrong", "silly")
        self.assertEqual(account, False)
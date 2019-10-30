from app.models import User,Role
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_role = Role(name="adm")
        self.new_user = User(username="ray",email="myemail@gmail.com",password="123",role=self.new_role)

    #def tearDown(self):
    #    Role.query.delete()
    #    User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.username,"ray")
        self.assertEquals(self.new_user.email,"myemail@gmail.com")

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('123'))
    

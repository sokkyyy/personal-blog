from app.models import User,Post,Role
import unittest

class TestPost(unittest.TestCase):
    def setUp(self):
        self.new_role = Role(name="adm")
        self.new_user = User(username="ray",email="myemail@gmail.com",password="123",role=self.new_role)
        self.new_post = Post(title="super",content="wwwwwww",user=self.new_user)
    
    def test_post_instances(self):
        self.assertEquals(self.new_post.title,"super")
        self.assertEquals(self.new_post.content,"wwwwwww")

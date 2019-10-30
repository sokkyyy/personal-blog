from app.models import User,Post,Role,Comment
import unittest

class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_role = Role(name="adm")
        self.new_user = User(username="ray",email="myemail@gmail.com",password="123",role=self.new_role)
        self.new_post = Post(title="super",content="wwwwwww",user=self.new_user)
        self.new_comment = Comment(comment='f',user=self.new_user,post=self.new_post)
    
    def test_comment_instance(self):
        self.assertEquals(self.new_comment.comment, 'f')
        


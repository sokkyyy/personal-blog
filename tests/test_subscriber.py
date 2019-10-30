from app.models import Subscriber
import unittest

class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.new_sub = Subscriber(email="myemail@gmail.com")
    
    def test_sub_instance(self):
        self.assertEquals(self.new_sub.email,"myemail@gmail.com")
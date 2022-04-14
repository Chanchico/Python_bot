import unittest
import sys
sys.path.append("..")
from object import Object

class TestObject(unittest.TestCase):
    def setUp(self):
        self.o = Object(10, 20) 

    def test_object_is_instance_of_object(self):
        self.assertIsInstance(self.o, Object)


if __name__ == '__main__':
    unittest.main()
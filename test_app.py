import unittest
from app import add

class TestApp(unittest.TestCase):
    def Test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(2,0),2)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(2,-1),1)
        
if __name__ == '__main__':
    unittest.main()
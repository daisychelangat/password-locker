import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User('daisychelangat','284565q')
    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
      
        self.assertEqual(self.new_user.username,'daisychelangat')
        self.assertEqual(self.new_user.password,'284565q')



if __name__ == '__main__':
        unittest.main()

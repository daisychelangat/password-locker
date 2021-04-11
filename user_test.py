import unittest
from user import User
from user import Credentials

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
        self.new_user = User('daisychelangat','200084565q')
    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
       self.assertEqual(self.new_user.username,'daisychelangat')
       self.assertEqual(self.new_user.password,'200084565q')

    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has been created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):   
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        '''
        Method that runs before each individual credentials test methods run.
        '''
        self.new_credentials = Credentials('dee','daisychelangat','200084565q')

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_details(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        
        self.assertEqual(self.new_credentials.account,'dee')
        self.assertEqual(self.new_credentials.username,'daisychelangat')
        self.assertEqual(self.new_credentials.password,'200084565q') 

    def test_save_credentials(self):
        """
        test case to test if the credential object is saved into the credentials list.
        """
        self.new_credentials.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    
    def test_save_many_account(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_user_credentials()
        test_creditial = Credentials('dee','daisychelangat','200084565q')
        test_creditial.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_find_creditial(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        
        self.new_credentials.save_user_credentials()
        test_creditial = Credentials('dee','daisychelangat','200084565q')
        test_creditial.save_user_credentials()

        the_creditial = Credentials.find_by_number("dee")
        self.assertEqual(the_creditial.account,test_creditial.account)

    def test_creditial_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credentials.save_user_credentials()
        test_creditial = Credentials('dee','daisychelangat','200084565q')
        test_creditial.save_user_credentials()
        
        found_credential = Credentials.credentials_exist("dee")
        self.assertTrue(found_credential)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credentials.save_user_credentials()
        test_creditial = Credentials('dee','daisychelangat','200084565q')
        test_creditial.save_user_credentials()
        
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)




if __name__ == '__main__':
        unittest.main()

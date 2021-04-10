class User:
    """
    Class that generates new instances of users and respective passwords
    """
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def save_user(self):
        '''
        save_user method saves a new user object to user list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method deletes a saved user from user_list
        '''
        User.user_list.remove(self)

#    @classmethod
#     def display_user(cls):
#         return cls.user_list
class Credentials:
    credentials_list = []
    def __init__(self,account,username,password):
        self.account = account
        self.password = password
        self.username = username
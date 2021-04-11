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

#  @classmethod
#     def verify_user(cls,username,password):
#         a_user = ''
#         for user in User.user_list:
#             if(user.username == username and user.password == password):
#                 a_user == user.username
#                 return a_user
    def save_user_credentials(self):
        '''
        save_user_credential method saves a new user object to credentials list
        '''
        Credentials.credentials_list.append(self)
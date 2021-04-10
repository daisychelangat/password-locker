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
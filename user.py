class User:
    """
    Class that generates new instances of users and respective passwords
    """
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
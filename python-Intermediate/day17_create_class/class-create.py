
class User:
    def __init__(self, id, username) :  # this __init__ function runs everytime an object gets created.
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):      # creating a function to follow someone using their username
        user.followers += 1      
        self.following += 1    

user_1 = User("001", "Viral")
user_2 = User("002", "Mikin")

user_1.follow(user_2)

###################################################################################





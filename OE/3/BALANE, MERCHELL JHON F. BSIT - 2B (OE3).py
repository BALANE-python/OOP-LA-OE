class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def login(self):
        print(f"{self.username} logged in!")
    
    def post(self):
        print(f"{self.username} posted something!")
    
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, fol_num):
        super().__init__(username, password)
        self.fol_num = fol_num
        
    def share_story(self):
        print(f"{self.username} shared a story with {self.fol_num} followers!")
    
class XAccount(SocialMediaAccount):
    def __init__(self, username, password, fol_twts):
        super().__init__(username, password)
        self.fol_twts = fol_twts
        
    def tweet(self):
        print(f"{self.username} tweeted to {self.fol_twts} followers!")
    

ig_acc = InstagramAccount("mrchll_lol", "1234", 120)
x_acc = XAccount("mrchll_lol", "2004", 56)


ig_acc.login()
ig_acc.share_story()

x_acc.login()
x_acc.tweet()

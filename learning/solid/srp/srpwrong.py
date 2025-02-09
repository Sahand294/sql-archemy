class User:
    def __init__(self,username,passport):
        self.name = username
        self.passport = passport
    def register(self):
        print(f'user {self.name} is regissterd')
    def login(self):
        print(f'user {self.name} is loged in')
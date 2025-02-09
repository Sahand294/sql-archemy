class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class UserRegister:
    def register(self, user: User):
        print(f'{user.name} is registered')


class UserLogin:
    def login(self, user: User):
        print(f'{user.name} is login')

class MessageBored:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

user1 = MessageBored('Sahand', 1233938, 'sahand@example.com')
user1list = [user1.name,user1.id,user1.email]
user2 = MessageBored('Radman', 721758, 'radman@example.com')
user2list = [user2.name,user2.id,user2.email]
class Messager:
    def __init__(self,message,user):
        print('\n',user.name)
        print(f'"{message}"')
        print(f'\nID:{user.id}')
        print(f'EMAIL:{user.email}')
Messager('hey wanna go to the park?',user1)
Messager('sure',user2)
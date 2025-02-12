from random import randint
from registering import Register
class Game:
    def __init__(self,username):
        num = int(randint(0,2))
        a = 0
        Notdone = True
        while Notdone:
            i = input('guess the number:')
            if int(i) >num:
                a += 1
                print('lower')
            elif int(i) < num:
                a += 1
                print('higher')
            elif int(i) == num:
                Register(username,a)
                Notdone = False
Game('sahand')

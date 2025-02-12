from projects.guessing_game.prostgresssql.total import DataBase
from datetime import datetime
class Register:
    def __init__(self,username,attempts):
        time = datetime.now()
        DataBase.insert('accounts','username,attempts,time',f"('{username}',{attempts},'{time.strftime('%Y:%m:%d %H:%M:%S')}')")
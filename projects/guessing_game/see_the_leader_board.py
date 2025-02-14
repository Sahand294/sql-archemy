from projects.guessing_game.prostgresssql.total import DataBase
class See:
    @staticmethod
    def see():
        r = DataBase.read(f'accounts ORDER BY attempts')
        return r
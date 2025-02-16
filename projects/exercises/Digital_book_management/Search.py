from projects.exercises.prostgresssql.total import DataBase
class Search:
    @staticmethod
    def by_title(title):
        r = DataBase.read(f"digital_book WHERE title = '{title}'")
        return r
    @staticmethod
    def by_author(author):
        r = DataBase.read(f"digital_book WHERE author = '{author}'")
        return r
    @staticmethod
    def publish_Date(date):
        r = DataBase.read(f"digital_book WHERE publish_date = '{date}'")
        return r
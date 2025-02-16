from adding_book import Adding_book
from datetime import datetime
from Search import Search
class Book:
    def __init__(self,title,author):
        d = datetime.now()
        u = d.strftime('%Y:%m:%d %H:%M:%S')
        self.title = title
        self.author = author
        Adding_book.database(title,author,u)
        Adding_book.json(title,author,u)
Book('sahands','radins')
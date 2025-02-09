class Book:
    def __init__(self, title, author, category, id):
        self.title = title
        self.author = author
        self.category = category
        self.id = id
        self.borrow = False

    def borrowing_books(self):
        self.borrow = True
        # self.borrowedbook = book


class Library:
    def __init__(self):
        self.categorys = {}
        self.books = []

    def adding_categorys(self, categoryname):
        if categoryname in self.categorys:
            raise Exception('category already exists in the libarery')
        self.categorys[categoryname] = Category(categoryname)

    def add_books(self, title, author, id, categoryname):
        if categoryname not in self.categorys:
            raise Exception('there is no such category')
        getcategory = self.categorys[categoryname]
        books = Book(title, author, getcategory, id)
        getcategory.adding_bookss(books)
        self.books.append(books)
    def show_inventory(self):
        if not self.books:
            print('liberary is empty')
        else:
            for x in self.books:
                print(x.title)

class Category:
    def __init__(self, name):
        self.name = name
        self.books = []

    def adding_bookss(self, book):
        self.books.append(book)

    def removing_books(self, book):
        self.books.remove(book)
libery = Library()
libery.adding_categorys('math')
libery.adding_categorys('science')
libery.add_books('2+2','einstein',135725,'mat')
libery.show_inventory()

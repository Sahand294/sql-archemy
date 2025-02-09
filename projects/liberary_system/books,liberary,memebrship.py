from  searching_books import Search_books
from searching_members import Search_Member
from books import  Books
from member_Ship import Membership
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}




    def returning_books(self, member_id, book_isbn):
        Search_Member.check_if_member_Exists(member_id,self.members)
        Search_books.check_if_book_Exists(book_isbn,self.books)
        if book_isbn not in self.members[member_id]['books borrowed']:
            raise ValueError(f'member does not have the book!')
        self.members[member_id]['books borrowed'].remove(book_isbn)
        self.books[book_isbn]["quantity's"] += 1

    def borrowing_Books(self, member_id, book_isbn):
        Search_Member.check_if_member_Exists(member_id,self.members)
        Search_books.check_if_book_Exists(book_isbn,self.books)

        if book_isbn in self.members[member_id]['books borrowed']:
            raise ValueError(f'they already have the book')
        if self.books[book_isbn]["quantity's"] == 0:
            raise ValueError(f'no more books left!')


        if len(self.members[member_id]['books borrowed']) == 3:
            raise ValueError(f'the limit for borrowing books has been reached!')


        self.members[member_id]['books borrowed'].append(book_isbn)
        self.books[book_isbn]["quantity's"] -= 1

    def add_book(self, book):
        if not isinstance(book,Books):
            raise ValueError('no such book at all')
        isbn = book.isbn
        title = book.title
        author = book.author
        number_of_copy_left = book.quantity
        if isbn in self.books:
            raise KeyError(f'the book {title} by the id {isbn} already exist.')
        book = Books(title, author, isbn, number_of_copy_left)
        self.books[isbn] = {'title': title, 'author': author, 'isbn': isbn, "quantity's": book.quantity}

    def add_member(self, member):
        if not isinstance(member,Membership):
            raise ValueError('no such member at all')
        if id in self.members:
            raise KeyError(f'the member:{member.name} by the id:{member.id} already exist')
        self.members[member.id] = {'name': member.name, 'id': member.id, 'books borrowed': []}

    def removing_books(self, isbn):
            if isbn in self.books:
                del self.books[isbn]
                for i in self.members:
                        if isbn in self.members[i]['books borrowed']:
                            self.members[i]['books borrowed'].remove(isbn)
            else:
                raise KeyError(f'no such book')

    def removing_members(self, id):
            if id in self.members:
                del self.members[id]
            else:
                raise KeyError(f'no such member')
l = Library()
sahand = Membership('sahand',1)
book1 = Books('boy','john boyne',1,10)
book2 = Books('girl','john boyne',2,99)
l.add_member(sahand)
l.add_book(book2)
l.add_book(book1)
print(Search_books.search_book_by_author('john boyne',l.books))
l.borrowing_Books(1,1)

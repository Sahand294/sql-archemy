class Search_books:
    @staticmethod
    def check_if_book_Exists(isbn, book_list):
        if isbn not in book_list:
            raise ValueError(f'there is no such book')

    @staticmethod
    def search_book_by_title(name, book_list):
        try:
            for i in book_list:
                if book_list[i]['title'] == name:
                    return book_list[i]
        except:
            raise Exception('no such book!')

    @staticmethod
    def search_book_by_isbn(isbn, book_list):
        try:
            for i in book_list:
                if i == isbn:
                    return book_list[i]
        except:
            raise Exception('no such book!')

    @staticmethod
    def search_book_by_author(author, book_list):
        books = []
        for i in book_list:

            if book_list[i]['author'] == author:
                books.append(book_list[i])
        if len(books) == 0:
            raise Exception('no such book!')
        return books

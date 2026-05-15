from lib.book import *

class BookRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        
        #1 All - Return all columns from books table
        rows = self.connection.execute("SELECT * FROM books")
        books_list = []
        
        for book in rows:
            item = Book(book["title"], book["author"], book["id"])    
            books_list.append(item)
        return books_list


        #2 Return a single book by ID
        #3 Add a new book
    def create(self, book):
            self.connection.execute("INSERT INTO books (title, author) VALUES (%s, %s)", [
                                    book.title, book.author])
            
   

        #4 Create a new row with a new book 
        
        # """
        # Use book repo to:
        # 1. Get list of all books, and render this on the home page
        # 2. Let the client search for books, and display through GET request
        # 3. Add new books, through a POST request
        # 4. Delete books, through DELETE request 
        # """
        
    


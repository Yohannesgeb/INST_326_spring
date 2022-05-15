# Import sys lib
import argparse
from itertools import count
import re
import sys
import operator
from typing import overload

from numpy import append

class Book:
    """Any type of book.

    Attributes:
        Book ID (int): Unique ID number of the indivdual books that are
        avaliable, expressed as integers.

        Title (str): The title of the individual books represented as a string.

        Publication year (int): The year the indivdual book was published, 
        expressed by a 4-digit integer.

        Type (str): Type of a book, expressed as string value.

        Overdue price (float): Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float.
        Default float value is 0.

        Days until due (str): -1 when it has not been rented out.

        Days of overdue (int): Number of overdue days, expressed as
        integer value. Default value is 0.
        """

    def __init__(self, book_id, title, pub_year, type, overdue_price = 0,
                    due_days = -1, overdue_days = 0):
        """Initialize a Book object.

        Args:
            book_id (int): ID of indivdual book

            Title (str): Title of book_id

            pub_year (int): Year as 4 digit integer representing the
            publication of the book.

            overdue_price (float): A float that is determined by
            (rent_dur - rented_days) * price. Default to 5.

            rent_dur (int): The amount of days the borrower chose to
            rent a book.
        """
        self.book_id = book_id
        self.type = type
        self.title = title
        self.pub_year = pub_year
        self.overdue_price = overdue_price
        self.due_days = due_days
        self.overdue_days = overdue_days
        if due_days == 0:
            self.overdue_price = self.overdue_days * 5
    
    def __str__(self):
        """ Initialize the book object as a string 
            return(str): book id and book title
        """
        str = (f"Book ID: {self.book_id} / "
               f"Book title: {self.title}"
               )
        return str

    def rented(self):
        """ due days of books in the book object = 7 days """
        self.due_days = 7

    def returned(self):
        """ represent the returned books in the book object
        Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float.
        Default float value is 0.  -1 when it has not been rented out.
        Number of overdue days, expressed as
        integer value. Default value is 0.
       
             return(bool):True 
        """
        if self.overdue_price == 0:
            self.due_days = -1
            self.overdue_days = 0
            return True
class Paper_book(Book):
    """Paper Book inhrita the book object and all its attributes 
        Attributes
        Book ID (int): Unique ID number of the indivdual books that are
        avaliable, expressed as integers.

        Title (str): The title of the individual books represented as a string.

        Publication year (int): The year the indivdual book was published, 
        expressed by a 4-digit integer.

        Type (str): Type of a book, expressed as string value.

        Overdue price (float): Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float.
        Default float value is 0.

        Days until due (str): -1 when it has not been rented out.

        Days of overdue (int): Number of overdue days, expressed as
        integer value. Default value is 0.
    """
    def __init__(self, book_id, title, pub_year, type = "paper_book", 
                overdue_price = 0, due_days = -1, overdue_days = 0):
        """ Initialize a paper_Book object.
        Args:
            book_id (int): ID of indivdual book

            Title (str): Title of book_id

            pub_year (int): Year as 4 digit integer representing the
            publication of the book.

            type(str): Type of a book, expressed as string value.

            overdue_price (float): A float that is determined by
            (rent_dur - rented_days) * price. Default to 5.

            due_days(int): -1 when it has not been rented out.

            overdue_days(int): Number of overdue days, expressed as
        integer value. Default value is 0.

        """
        super().__init__(book_id, title, pub_year, type, overdue_price,
                due_days, overdue_days)
    
    def __str__(self):
        """Initialize the Paper_book object as a string 
            return(str): Paper book id and  title
        """
        str = (f"Paper Book ID: {self.book_id}"
               f"Paper Book title: {self.title}")
        return str

class Audio_book(Book):
    """Audio Book inhrita the book object and all its attributes 

        Attributes: 
        Book ID (int): Unique ID number of the indivdual books that are
        avaliable, expressed as integers.

        Title (str): The title of the individual books represented as a string.

        Publication year (int): The year the indivdual book was published, 
        expressed by a 4-digit integer.

        Type (str): Type of a book, expressed as string value.

        Overdue price (float): Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float.
        Default float value is 0.

        Days until due (str): -1 when it has not been rented out.

        Days of overdue (int): Number of overdue days, expressed as
        integer value. Default value is 0.
    """
    def __init__(self, book_id, title, pub_year, type = "audio_book", 
                overdue_price = 0, due_days = -1, overdue_days = 0):
        """ Initialize a audio_Book object 
      Args:
            book_id (int): ID of indivdual book

            Title (str): Title of book_id

            pub_year (int): Year as 4 digit integer representing the
            publication of the book.

            type(str):audio_book

            overdue_price (float): A float that is determined by
            (rent_dur - rented_days) * price. Default to 5.

            due_days(int):-1 when it has not been rented out.

            overdue_days(int): Number of overdue days, expressed as
        integer value. Default value is 0.
        """
        super().__init__(book_id, title, pub_year, type, 
                overdue_price, due_days, overdue_days)

    def rented(self):
        """Determined rice of book by (rent_dur - rented_days) * price. Default to 5.

           side effects:
                     print out price of overdue books
        """
        self.overdue_price = super().overdue_price + 5
        print (f"Rented, Renting cost is $5. And this is your overdue price ${self.overdue_price}")
    
    def __str__(self):
        """ Initialize the Audio_book object as a string 
        
             return(str):Audio books id and title
       
        """
        str = (f"Audio Book ID: {self.book_id} \ "
               f"Audio Book title: {self.title}")
        return str
#Functions
def book_info(books):
    """ Books information on (book id, title, type, published year)  
    Args:
        books(str): instance of books  
    
    side effects: 
                increment books and prince book id and title
    """
    count = 1
    for book in books:
        if ((not isinstance(book, Book)) and 
            (not isinstance(book, Audio_book)) and
            (not isinstance(book, Paper_book))):
                    print('This Book is not a Book object')
                    books.remove(book)
                    return
        str = f"Book {count}. ({book.__str__()})"
        print(str)
        count += 1

def rent_book(books, rented, book):
    """ Check if a Book is rented
    Args:
        books(str): instance of books  
        
        rented(list): list of books that are rented out 
        
        book(str):instance of books in Book object 
    """
    for a in books:
        if a.book_id == book.book_id:
            books.remove(a)
            rented.append(a)
            rented.sort(key=lambda x: x.book_id)
            print(f'You have rented {book.title}'
                  f'with Book ID# {book.book_id}')
            return

def return_book(books, rented, book):
    """ check if a book is returned 
    
    Args:

        books(str): instance of books 

        rented(list): list of books that are rented out 

        book(str):instance of books in Book object 

        return(str)
    
    """
    for a in rented:
        if a.book_id == book.book_id:
            rented.remove(a)
            books.append(a)
            books.sort(key=lambda x: x.book_id)
            print(f'You have returned {book.title}'
                  f'with Book ID# {book.book_id}')
            return
def sort_books(date):
    """ sort books by the date 
        Args:
            date(int): book published date
        
        side effect: print out list of book sorted by published date 
    """
    with open(filepath, "r", encoding="utf-8") as f:
        date = f.read(delimiter = ',')
        sort = sorted(date,key = operator.itemgetter(2))
        for eachline in sort:
            print (eachline)

def main(filepath):
    """
       Args:
            filepath(): open the file for reading list comprehension to build the list of Book objects.
       
       side effects: prompted to make an input as either option 1 to rent a book or option 2 to return a book

    """
    nr_books = list()   #list of not rented books
    r_books = list()    #list of rented books
    p_books = list()   #list of paper books
    a_books = list()    #list of audio books
    books = list()
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            (book_id, title, pub_year, book_type , 
            overdue_price , due_days , overdue_days) = line.strip().split(',')
            book_id = int(book_id)
            pub_year = int(pub_year)
            overdue_price = float(overdue_price)
            due_days = int(due_days)
            overdue_days = int(overdue_days)
            book = Book(book_id, title, pub_year, book_type ,
            overdue_price , due_days , overdue_days)
            audio = Audio_book(book_id, title, pub_year, book_type ,
            overdue_price , due_days , overdue_days)
            paper = Paper_book(book_id, title, pub_year, book_type ,
            overdue_price , due_days , overdue_days)
            nr_book = Book(book_id, title, pub_year, book_type ,
            overdue_price , due_days , overdue_days)
            r_book = Book(book_id, title, pub_year, book_type ,
            overdue_price , due_days , overdue_days)
            books.append(book)
            if book_type == "audio_book":
                a_books.append(audio)
                a_books.sort(key=lambda x: x.book_id)
            if book_type == "paper_book":
                p_books.append(paper)
                p_books.sort(key=lambda x: x.book_id)
            if int(due_days) == -1:
                nr_books.append(nr_book)
                nr_books.sort(key=lambda x: x.book_id)
            if int(due_days) >= 0:
                r_books.append(r_book)
                r_books.sort(key=lambda x: x.book_id)
    while True:
        print ('\n===== Books Menu ======\n'
               'Select Option: (1) View books '
               '(2) Rent/Return Books '
               '(3) Exit the program')
        user = int(input('\nUSER INPUT: '))
        if user == 1:
            print('\n====== View Books ======\n'
                    '====== All Books ======\n')
            books.sort(key=lambda x: x.book_id)
            count = 1
            for book in books:
                str = (f"Book {count}. (Book ID: {book.book_id} / "
                       f"Book title: {book.title} / "
                       f"Book published year: {book.title} / "
                       f"Book type: {book.type} / "
                       f"Book overdue price: {book.overdue_price} / "
                       f"Book due days: {book.due_days} / "
                       f"Book overdue days: {book.overdue_days})"
                    )
                print(str)
                count += 1
            print('Select Option: (1) Not Rented (2) Rented (3) Audio'
            ' (4) Paper')
            user1 = int(input('\n-----USER INPUT: '))
            if user1 == 1:
                print('\n====== Not Rented ======\n')
                book_info(nr_books)
            elif user1 == 2:
                print('\n====== Rented ======\n')
                book_info(r_books)
            elif user1 == 3:
                print('\n====== Audio ======\n')
                book_info(a_books)
            elif user1 == 4:
                print('\n====== Paper ======\n')
                book_info(p_books)
            else:
                print('INVALID USER INPUT')
        elif user == 2:
            print('\n====== Rent/Return ======\n')
            print('Select Option: (1) Rent (2) Return')
            user1 = int(input('-----USER INPUT: '))
            if user1 == 1:
                print('\n====== Rent ======\n')
                print('\nAvailable Books to rent\n')
                book_info(nr_books)
                user2 = int(input("\n-----ENTER BOOK ID: "))
                for book1 in nr_books:
                    if book1.book_id == user2:
                        rent_book(nr_books, r_books, book1)
                        break
            elif user1 == 2:
                print('\n====== Return ======\n')
                print('\n====== Rented Books ======\n')
                book_info(r_books)
                user2 = int(input("\n-----ENTER BOOK ID: "))
                for book1 in r_books:
                    if book1.book_id == user2:
                        return_book(nr_books, r_books, book1)
                        break
            else:
                print('INVALID USER INPUT')
        elif user == 3:
            return
        else:
            print('INVALID USER INPUT. Please try again.')

if __name__ == "__main__":
    filepath = "books.csv" # main(filepath) can be called to run the program. filepath is a text file
    main(filepath)
    parser = argparse.ArgumentParser()  # main(filepath) can be called to run the program. filepath is a text file
    parser.add_argument()
    parser.add_argument()

   
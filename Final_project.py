# Import sys lib
import argparse
import re
import sys
from typing import overload

class Book:
    """The class Book has access to book_id, title, pub_year, 
    overdue_price, rented_days operations.

    Attributes:
        Book ID (int): Unique ID number of the indivdual books that are
        avaliable, expressed as integers.

        Type (str): Type of a book, expressed as a string value. Defaulted to
        "book".

        Title (str): The title of the individual books represented as a string.

        Publication year (int): The year the indivdual book was published, 
        expressed by a four digit integer.

        Overdue price (float): Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float. Defaulted to 0.

        rented_days (int): Rental duration represents how long the
        borrower rented the books, default integer value is 7.
        """

    def __init__(self,type,book_id,title,pub_year,overdue_price,due_days):
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
        type = "book"
        overdue_price = 0
        due_days = -1
        self.book_id = book_id
        self.type = type
        self.title = title
        self.pub_year = pub_year
        self.overdue_price = overdue_price
        self.due_days = due_days

    def rented(self):
        self.due_days = 7
        print("")
        return True

    def overdue(self):
                
        """Checks if the book chosen is overdue or not based on the 
            remaining days.

            Returns: A boolean, if (rent_dur - rented_days) < 0 then it
            is True, otherwise False. (True = overdue, False = not overdue)
        """

        if 0 > self.rent_dur - self.rented_days:
            return True
        else:
            return False

class Audio_Book(Book):
    """ Overdue_Book class inheritance from the Book classs """
    def __init__(self, type):
        type = "audio_book"
        super().__init__()
        self.type = type

    def rented()
        
        
def isOnline():




        
def rent_book(books, rented_books, book_id):
    if isinstance(books, Book) & isinstance(rented_books, Book):
        for book in books:
            if book.book_id == book_id:

    """The rent_book functio takes (int) value book_id to retrive
    Args:
        rent(int): Takes in integer value argument book_id to retrieve book_id
    # Rents a book from the library by subtracting from a list of shelved Book
    
    return:
        a list of rented Book.
    
      """

def return_book(books, overdue, book_id):
    """The return_book function

    Args:
        book_id; Takes in integer value argument book_id to retrieve book_id
    
    
    Return:
             a book from the library by subtracting from list of rented Book
             and add a Book to a list of shelved Book.
     """

def main(filepath):
    """The main function 
    
    Args:
        filepath 
        # Create an empty list of Book named rented, Create an empty
        # list of Book named shelved
        # Create an empty list of Overdue_Book named overdue_books
        # Lists are all immutable.

        # Use with function to unpack the given text file (filepath)
        # then using for in loop to set each line as a Book object
        # (When creating it, if the book is overdue (rented_days is 
        # negative value), instead of setting it to a Book object, set it to
        # Overdue_Book object). Use if conditional to check whether each line
        # or a book of the text file is rented or not. If rented, add the book
        # to the rented list. Else, shelved list. For Overdue)Book objects,
        # instead of adding to either list, append it to overdue list.

        # Assign variables to length of each list
        # Assign a variable "total" to a sum of "rented" list length and
        # "shelved" list length.
        # Call rent_book function(book_id) && return_book(book_id) 
        # with book_id that are available in each list.

    Returns: 
        fstring that contains information about total number of
        books, total rented books, total shelved books, and
        total overdue books.
 """
    book = Book ([])
    due = Overdue_Book()
    done = False
    while done == False:
        print ('===== Books Menu ======')
    user = int(input("Enter choice"))


if __name__ == "__main__":
    filepath = ".txt file"
    main(filepath)
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()
# main(filepath) can be called to run the program. filepath is a text file
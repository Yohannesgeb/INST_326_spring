# Import sys lib
import re
import sys
from typing import overload
class Book:
    # Parent-class Book that has
    # Attributes:
    # book_id (int, ID # of a book - integer)
    # title (str, title of a book)
    # pub_year (int, Published Year of the Book)
    # overdue_price (float, Overdue price per day late)
    # rent_dur (Rental duration, default to integer value of 7)
    # rented (Rented or not, boolean - True = rented / False = shelved)

    def __init__(self, book_id, title, pub_year, overdue_price, rented_days):
        # arguments: book_id (int), title (str), pub_year(int)
        # overdue_price(float), rented_days (bool)
        self.book_id = book_id # book_id (int, ID # of a book - integer)
        self.title = title # title (str, title of a book)
        self.pub_year = pub_year # pub_year (int, Published Year of the Book)
        self.overdue_price = overdue_price # overdue_price (float, Overdue price per day late)
        self.rented_days = rented_days # rent_dur (Rental duration, default to integer value of 7)
        self.rent_dur = 7 # rent_dur (Rental duration, default to integer value of 7)
        if self.rented_days == 0: # rented (Rented or not, boolean - True = rented / False = shelved)
            self.rented = False
        else:
            self.rented = True

    def overdue(self):
        # Checks whether the book is overdue or not by checking days remaining, 
        # returns a boolean (True = overdue rent_dur (int 7) - rented_days,
        # False = not overdue)
        if 0 > self.rent_dur - self.rented_days:
            return True
        else:
            return False

# Overdue_Book is a Child class of a parent class Book
class Overdue_Book(Book):
    """ Overdue_Book class inheritance from the Book classs """
    # __init__() doesn't change && overdue() doesn't change
    def money_owed(self):
        """" money_owed methode calculates money owed for overdue books
            overdue_books takes in no argument Calculates money owed when books are overdue
        
        return: amount owed of overdue books 
        
        """
        overdue = self.rented_days - self.rent_dur
        return overdue * self.overdue_price

def rent_book(book_id):
    """The rent_book functio takes (int) value book_id to retrive
    Args:
        rent(int): Takes in integer value argument book_id to retrieve book_id
    # Rents a book from the library by subtracting from a list of shelved Book
    
    return:
        a list of rented Book.
    
      """

def return_book(book_id):
    """The return_book function 

    Args:
        book_id; Takes in integer value argument book_id to retrieve book_id
    
    
    Return:
             a book from the library by subtracting from list of rented Book and add a Book to a list of shelved Book.
     """

def main(filepath):
    """The main function 
    
    Args:
        filepath 
        # Create an empty list of Book named rented, Create an empty list of Book
        # named shelved
        # Create an empty list of Overdue_Book named overdue_books
        # Lists are all immutable.

        # Use with function to unpack the given text file (filepath)
        # then using for in loop to set each line as a Book object (When creating
        # it, if the book is overdue (rented_days is negative value), instead of
        # setting it to a Book object, set it to Overdue_Book object).
        # Use if conditional to check whether each line or a book of the text
        # file is rented or not. If rented, add the book to the rented list.
        # Else, shelved list. For Overdue)Book objects, instead of adding to either
        # list, append it to overdue list.

        # Assign variables to length of each list
        # Assign a variable "total" to a sum of "rented" list length and
        # "shelved" list length.
        # Call rent_book function(book_id) && return_book(book_id) with book_id
        # that are available in each list.

        # Returns fstring that contains information about total number of books,
        # total rented books, total shelved books, and total overdue books.
 """
    book = Book ([])
    due = Overdue_Book()
    done = False
    while done == False:
        print ('===== Books Menu ======')
    user = int(input("Enter choice"))


if __name__ == "__main__":
     main(filepath)
    # main(filepath) can be called to run the program. filepath is a text file
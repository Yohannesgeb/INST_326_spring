'''This is a file for our final project'''
# Import Argument Parser class

class Book:
    # Parent-class Book that has
    # Attributes:
    # book_id (ID # of a book - integer)
    # title (title of a book)
    # pub_year (Published Year of the Book)
    # overdue_price (Overdue price per day late)
    # rent_dur (Rental duration, default to integer value of 7)
    # rented (Rented or not, boolean - True = rented / False = shelved)

    def __init__(self, book_id, title, pub_year, overdue_price, rented_days):
        # arguments: book_id (int), title (str), pub_year(int)
        # overdue_price(int), rented_days (bool)
        self.book_id = book_id
        self.title = title
        self.pub_year = pub_year
        self.overdue_price = overdue_price
        self.rented_days = rented_days
        self.rent_dur = 7
        if self.rented_days == 0:
            self.rented = False
        else:
            self.rented = True

    def overdue(self):
        # Checks whether the book is overdue or not by checking days remaining, 
        # returns a boolean (True = overdue, False = not overdue)
        if 0 > self.rent_dur - self.rented_days:
            return True
        else:
            return False

# Overdue_Book is a Child class of a parent class Book
class Overdue_Book(Book):
    # __init__() doesn't change
    # overdue() doesn't change
    def money_owed(self):
        # takes in self as argument and calculates money owed when books are
        # overdue
        overdue = self.rented_days - self.rent_dur
        return overdue * self.overdue_price

def rent_book(book_id):
    # Takes in integer value argument book_id to retrieve book_id
    # Rents a book from the library by subtracting from a list of shelved Book
    # and add to a list of rented Book.

def return_book(book_id):
    # Takes in integer value argument book_id to retrieve book_id
    # Returns a book from the library by subtracting from list of rented Book
    # and add a Book to a list of shelved Book.

def main(filepath):
    # Create an empty list of Book named rented, Create an empty list of Book
    # named shelved

    # Use with function to unpack the given text file (filepath)
    # and use if conditional to check whether each line or a book of the text
    # file is rented or not. If rented, add the book to the returned list.
    # Else, shelved.

    # Assign variables to length of each list
    # Assign a variable "total" to a sum of "rented" list length and
    # "shelved" list length.
    # Call rent_book function(book_id) && return_book(book_id) 

    # Returns fstring that contains information about total number of books,
    # total rented books, total shelved books, and total overdue books.


if __name__ == "__main__":
    main()
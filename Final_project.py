'''This is a file for our final project'''
# Import Argument Parser class

class Book:
    def __init__(self, book_id, title, pub_year, overdue_price, rented_days):
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
        if 0 > self.rent_dur - self.rented_days:
            return True
        else:
            return False

class Overdue_Book(Book):
    def money_owed(self):
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
    # Takes in filepath as argument
    # Create an empty list of rented, Create an empty list of shelved

    # Use with function to unpack the given text file (filepath)
    # and use if conditional to check whether each line or a book of the text
    # file is rented or not. If rented, add the book to the returned list.
    # Else, shelved.

    # Assign variables to length of each list
    # Assign a variable "total" to a sum of "rented" list length and
    # "shelved" list length.
    # Call rent_book function(book_id) && return_book(book_id) 

    # Return fstring


if __name__ == "__main__":
    main()
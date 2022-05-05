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

        Title (str): The title of the individual books represented as a string.

        Publication year (int): The year the indivdual book was published, 
        expressed by a 4-digit integer.

        Type (str): Type of a book, expressed as string value. Default string
        value is "book".

        Copies (int): Number of Book's copies, expressed as int value.
        Default int value is 1.

        Days until due (str): -1 when it has not been rented out.

        Overdue price (float): Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float.
        Default float value is 0.

        Days of overdue (int): Number of overdue days, expressed as
        integer value. Default value is 0.
        """

    def __init__(self, book_id, title, pub_year, type = "book", copies = 1, 
                overdue_price = 0, due_days = -1, overdue_days = 0):
        """Initialize a Book object.

        Args:
            book_id (int): ID of indivdual book

            Title (str): Title of book_id

            pub_year (int): Year as 4 digit integer representing the
            publication of the book.

            num_books (int): Number of Copies, expressed as integer value.
            Default to 1.

            overdue_price (float): A float that is determined by
            (rent_dur - rented_days) * price. Default to 5.

            rent_dur (int): The amount of days the borrower chose to
            rent a book.
        """
        self.book_id = book_id
        self.type = type
        self.title = title
        self.pub_year = pub_year
        self.copies = copies
        self.overdue_price = overdue_price
        self.due_days = due_days
        self.overdue_days = overdue_days
        if due_days == 0:
            self.overdue_price = self.overdue_days * 5
    
    def __str__(self):
        return f"""Book({self.book_id}.\n
                   Book type: {self.type}.\n
                   Book title: {self.title}.\n
                   Book published year: {self.pub_year}.\n
                   Book copies: {self.copies}.\n
                   Book overdue price: {self.overdue_price}.\n
                   Book due days: {self.due_days}.\n
                   Book overdue days: {self.overdue_days}."""
    
    def __repr__(self):
        return f"""Book({self.book_id},{self.type},{self.title},
                   {self.pub_year},{self.copies},{self.overdue_price},
                   {self.due_days},{self.overdue_days})"""

    def rented(self):
        self.copies += 1
        self.due_days = 7

    def returned(self):
        if self.overdue_price == 0:
            self.copies += 1
            self.due_days = -1
            self.overdue_days = 0
            return True

    def overdue(self):
        self.due_days = 0
        self.overdue_price += 5

class Audio_book(Book):
    """ Overdue_Book class inheritance from the Book class """
    def __init__(self, type):
        type = "audio_book"
        super().__init__()
        self.type = type

    def rented(self):
        self.overdue_price = super().overdue_price + 5
        print (f"Rented, Renting cost is $5. And this is your overdue price ${self.overdue_price}")

#Functions
def isOnline():
    
def rent_book(books, rented, renting_book):
    if isinstance(renting_book, Book):
        if isinstance(books, list[Book]) & isinstance(rented, list[Book]):
            print("You can rent the book!")
    else:
        raise TypeError("Please enter a correct type")
    for book in books:
        if isinstance(book, Book):
            if book.book_id == renting_book.book_id:
                if book.copies > 1:
                    book.copies -= 1
                else:
                    books.remove(book)
    count = 0
    for rent in rented:
        if rent != rented[0]:
            count += 1
        if isinstance(rent, Book):
            if rent.book_id == renting_book.book_id:
                rent.copies += 1
                return
            else:
                if rented.index(rent) == count:
                    rented.append(rent)

def return_book(books, rented, return_book):
    if isinstance(return_book, Book):
        if isinstance(books, list[Book]) & isinstance(rented, list[Book]):
            print("You can return the book!")
    else:
        raise TypeError("Please enter a correct type")
    return_book.returned()
    for book in books:
        if isinstance(book, Book):
            if book.book_id == return_book.book_id:
                book.copies += 1
                num_cop = book.copies
    return_book.copies = num_cop
    books.append(return_book)
    changed = 0
    for rent in rented:
        if isinstance(rent, Book):
            if rent.book_id == return_book.book_id:
                changed += 1
                rent.copies -= 1
    if changed > 0:
        rented.remove(return_book)

def due_pay(book, pay):
    if isinstance(book, Book):
        book.overdue_price -= pay
    print(f"After paying ${pay}, your due balance is ${book.overdue_price}.")

def main(filepath):
    """The main function
    Recommended tasks:
    - Using with to extract the files accordingly
    - Create list of rented books and not rented books.
    - Change attributes accordingly like changing number of copies.
    - Renting a book out
    - Returning the book out
    
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
    nr_books = list()   #list of not rented books
    r_books = list()    #list of rented books
    na_books = list()   #list of not audio books
    a_books = list()    #list of audio books
    books = list()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            books.append(line)

if __name__ == "__main__":
    filepath = "books.csv"
    main(filepath)
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()
# main(filepath) can be called to run the program. filepath is a text file
    # main(filepath) can be called to run the program. filepath is a text file

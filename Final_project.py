# Import sys lib
import argparse
from itertools import count
import re
import sys
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

        Copies (int): Number of Book's copies, expressed as int value.
        Default int value is 1.

        Days until due (str): -1 when it has not been rented out.

        Overdue price (float): Overdue price of a book, price increases 
        per day late based on rent_dur, expressed as a float.
        Default float value is 0.

        Days of overdue (int): Number of overdue days, expressed as
        integer value. Default value is 0.
        """

    def __init__(self, book_id, title, pub_year, type, copies = 1, 
                overdue_price = 0, due_days = -1, overdue_days = 0):
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
        self.copies = copies
        self.overdue_price = overdue_price
        self.due_days = due_days
        self.overdue_days = overdue_days
        if due_days == 0:
            self.overdue_price = self.overdue_days * 5
    
    def __str__(self):
        return f"""Book ID: {self.book_id}.\nBook title: {self.title}.\n"""
    
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

class Paper_book(Book):
    """Paper Book

        Attributes:
    """
    def __init__(self, type = "paper_book"):
        super().__init__()
        self.type = type
    
    def __str__(self):
        return f"Paper Book ID: {self.book_id}.\nPaper Book title: {self.title}.\n"

class Audio_book(Book):
    """Audio Book

        Attributes:
    """
    def __init__(self, type):
        type = "audio_book"
        super().__init__()
        self.type = type

    def rented(self):
        self.overdue_price = super().overdue_price + 5
        print (f"Rented, Renting cost is $5. And this is your overdue price ${self.overdue_price}")
    
    def __str__(self):
        return f"Audio Book ID: {self.book_id}.\nAudio Book title: {self.title}.\n"

#Functions
def isOnline(book):
    """Books can be Online format or be Audio book.
    
    """
    if isinstance(book, Book):
        if book.type == "paper_book":
            book.type = "online_book"
            book.overdue_price = "10"
            book.due_days = "30"
            book.overdue_days = "0"

        if book.type == "audio_book":
            book.type = "online_audio_book"
            book.overdue_price = "15"
            book.due_days = "60"
            book.overdue_days = "0"

def rent_book(books, rented, renting_book):
    if isinstance(renting_book, Book):
        print("You can rent the book!")
    else:
        raise TypeError("Please enter a correct type")
    renting_book.rented()
    changed = 0
    for book in books:
        if isinstance(book, Book):
            if book.book_id == renting_book.book_id:
                changed += 1
                book.copies -= 1
    if changed > 0:
        books.remove(book)
    num_copies = 0
    for rent in rented:
        if isinstance(rent, Book):
            if rent.book_id == renting_book.book_id:
                rent.copies += 1
                num_copies += rent.copies
    renting_book.copies = num_copies
    rented.append(renting_book)

def return_book(books, rented, return_book):
    if isinstance(return_book, Book):
        if isinstance(books, list[Book]) & isinstance(rented, list[Book]):
            print("You can return the book!")
    else:
        raise TypeError("Please enter a correct type")
    return_book.returned()
    num_copies = 0
    for book in books:
        if isinstance(book, Book):
            if book.book_id == return_book.book_id:
                book.copies += 1
                num_copies += book.copies
    return_book.copies = num_copies
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
    
        Returns: 
    """
    nr_books = list()   #list of not rented books
    r_books = list()    #list of rented books
    p_books = list()   #list of paper books
    a_books = list()    #list of audio books
    books = list()
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days = line.strip().split(',')
            books.append(Book(book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days))
    for book in books:
        if book.type == "audio_book": # book.type == "online_audio_book":
            a_books.append(book)
        if book.type == "paper_book": # book.type == "online_book":
            p_books.append(book)
        if book.type == "notrented_book":
            nr_books.append(book)
        if book.type == "rented_book":
            r_books.append(book)
    a_count = 1
    for audio in a_books:
        print(f"Audio Book #{a_count}")
        str = audio.__str__()
        print(str)
        a_count+=1
    p_count = 1
    for paper in p_books:
        print(f"Paper Book #{p_count}")
        str = paper.__str__()
        print(str)
        p_count+=1
    nr_count = -1
    for rented_book in nr_books:
        print (f"Not rented book#{nr_count}")
        str = rented_book.__str__()
        print(str)
        nr_count += -1
    r_count = 1
    for rented_book in r_books:
        print (f"Rented Book #{r_count}")
        str = rent_book.__str__()
        print(str)
        r_books += 1
    
    
    while True:
        rent_book in r_books 
        print ('===== Books Menu ======')
        user = int(input("Enter choice: ")) 

        
        print ()
        #Rent/Return/due pay, etc. with user input. You want to print out
        #changes that you make or print the entire list?
        break
    return


  

    



if __name__ == "__main__":
    filepath = "books.csv"
    main(filepath)
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()
# main(filepath) can be called to run the program. filepath is a text file
    # main(filepath) can be called to run the program. filepath is a text file

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
        str = (f"Book ID: {self.book_id} / "
               f"Book title: {self.title}"
               )
        return str

    def rented(self):
        self.due_days = 7

    def returned(self):
        if self.overdue_price == 0:
            self.due_days = -1
            self.overdue_days = 0
            return True

class Paper_book(Book):
    """Paper Book

        Attributes:
    """
    def __init__(self, book_id, title, pub_year, type = "paper_book", 
                overdue_price = 0, due_days = -1, overdue_days = 0):
        super().__init__(book_id, title, pub_year, type, overdue_price,
                due_days, overdue_days)
    
    def __str__(self):
        str = (f"Paper Book ID: {self.book_id}"
               f"Paper Book title: {self.title}")
        return str

class Audio_book(Book):
    """Audio Book

        Attributes:
    """
    def __init__(self, book_id, title, pub_year, type = "audio_book", 
                overdue_price = 0, due_days = -1, overdue_days = 0):
        super().__init__(book_id, title, pub_year, type, 
                overdue_price, due_days, overdue_days)

    def rented(self):
        self.overdue_price = super().overdue_price + 5
        print (f"Rented, Renting cost is $5. And this is your overdue price ${self.overdue_price}")
    
    def __str__(self):
        str = (f"Audio Book ID: {self.book_id} \ "
               f"Audio Book title: {self.title}")
        return str
        
def rent_book(books, rented, book):
    for a in books:
        if a.book_id == book.book_id:
            books.remove(a)
            rented.append(a)
            rented.sort(key=lambda x: x.book_id)
            print(f'You have rented {book.title}'
                  f'with Book ID# {book.book_id}')
            return

def return_book(books, rented, book):
    for a in rented:
        if a.book_id == book.book_id:
            rented.remove(a)
            books.append(a)
            books.sort(key=lambda x: x.book_id)
            print(f'You have rented {book.title}'
                  f'with Book ID# {book.book_id}')
            return

def main(filepath):
    """The main function
    
        Returns: 
    """
    nr_books = list()   #list of not rented books
    r_books = list()    #list of rented books
    p_books = list()   #list of paper books
    a_books = list()    #list of audio books
    books = list()
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            book_id, title, pub_year, book_type , overdue_price , due_days , overdue_days = line.strip().split(',')
            book_id = int(book_id)
            pub_year = int(pub_year)
            overdue_price = float(overdue_price)
            due_days = int(due_days)
            overdue_days = int(overdue_days)
            book = Book(book_id, title, pub_year, book_type , overdue_price , due_days , overdue_days)
            audio = Audio_book(book_id, title, pub_year, book_type , overdue_price , due_days , overdue_days)
            paper = Paper_book(book_id, title, pub_year, book_type , overdue_price , due_days , overdue_days)
            nr_book = Book(book_id, title, pub_year, book_type , overdue_price , due_days , overdue_days)
            r_book = Book(book_id, title, pub_year, book_type , overdue_price , due_days , overdue_days)
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
            print('\n====== View Books ======\n')
            print('\n====== All Books ======\n')
            count = 1
            for book in books:
                str = f"Book#{count} {book.__str__()}"
                print(str)
                count += 1
            print('\nSelect Option: (1) Not Rented (2) Rented (3) Audio'
            '(4) Paper')
            user1 = int(input('\n-----USER INPUT: '))
            if user1 == 1:
                print('\n====== Not Rented ======\n')
                count1 = 1
                for book in nr_books:
                    str = f"#{count1}. {book.__str__()}"
                    print(str)
                    count1 += 1
            elif user1 == 2:
                print('\n====== Rented ======\n')
                count1 = 1
                for book in r_books:
                    str = f"#{count1}. {book.__str__()}"
                    print(str)
                    count1 += 1
            elif user1 == 3:
                print('\n====== Audio ======\n')
                count1 = 1
                for book in a_books:
                    str = f"#{count1}. {book.__str__()}"
                    print(str)
                    count1 += 1
            elif user1 == 4:
                print('\n====== Paper ======\n')
                count1 = 1
                for book in p_books:
                    str = f"#{count1}. {book.__str__()}"
                    print(str)
                    count1 += 1
        elif user == 2:
            print('\n====== Rent/Return ======\n')
            print('\nSelect Option: (1) Rent (2) Return')
            user1 = int(input('-----USER INPUT: '))
            if user1 == 1:
                print('\n====== Rent ======\n')
                print('\nAvailable Books to rent\n')
                count = 1
                for book in nr_books:
                    str = (f'({count}) Book ID: {book.book_id} \ '
                           f'Title: {book.title}')
                    print(str)
                    count += 1
                user2 = int(input("\n-----ENTER BOOK ID: "))
                for book1 in nr_books:
                    if book1.book_id == user2:
                        rent_book(nr_books, r_books, book1)
                        break
            elif user1 == 2:
                print('\n====== Return ======\n')
                print('\n====== Rented Books ======\n')
                count = 1
                for book in r_books:
                    str = (f'({count}) Book ID: {book.book_id} \ '
                          f'Title: {book.title}')
                    print(str)
                    count += 1
                user2 = int(input("\n-----ENTER BOOK ID: "))
                for book1 in r_books:
                    if book1.book_id == user2:
                        return_book(nr_books, r_books, book1)
                        break
            else:
                print('Invalid value input. Please try again.')
        elif user == 3:
            return
        else:
            print('Invalid value input. Please try again.')

if __name__ == "__main__":
    filepath = "books.csv"
    main(filepath)
    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()
# main(filepath) can be called to run the program. filepath is a text file
    # main(filepath) can be called to run the program. filepath is a text file

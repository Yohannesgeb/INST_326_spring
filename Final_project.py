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
        self.type = type
    
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
    if isinstance(book, Book) == False:
        
    count = 0
    for b in books:
        if b.book_id == book.book_id:
            if count == 0:
                books.remove(b)
                count = 1
    for r in rented:
        if r.book_id == a.book_id:
            num = r.copies + 1
    a.copies -= 1
    for r in rented:
        if r.book_id == a.book_id:
            r.copies = num
            count = 2
    if count == 2:
        print(f'You have rented {book.title}'
                f'with Book ID#{book.book_id}')
    # num_copies = 0
    # num = 0
    # pop = 0
    # for book in books:
    #     if pop == 0:
    #         if renting_book.book_id == book.book_id:
    #             a = books.pop(book)
    #             pop += 1
    #             book.copies -= 1
    #             num += book.copies
    #     else:
    #         book.copies = num
    # if a in rented:
    #     for rent in rented:
    #         if 
    # if renting_book in rented:
    #     rents = [a for a in rented if a.book_id == renting_book.book_id]
    #     for rent in rented:
    #         rent.copies += 1
    #         num_copies += rent.copies
    # renting_book.copies = num_copies
    # rented.append(renting_book)

def return_book(books, rented, return_book):
    if isinstance(return_book, Book):
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
            book_id = int(book_id)
            pub_year = int(pub_year)
            copies = int(copies)
            overdue_price = float(overdue_price)
            due_days = int(due_days)
            overdue_days = int(overdue_days)
            book = Book(book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days)
            audio = Audio_book(book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days)
            paper = Paper_book(book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days)
            nr_book = Book(book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days)
            r_book = Book(book_id, title, pub_year, book_type , copies , overdue_price , due_days , overdue_days)
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
        user = int(input('User input: '))
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
            user1 = int(input('User input: '))
            if user1 == 1:
                print('\n====== Not Rented ======\n')
                count1 = 1
                for book in nr_books:
                    str = f"Book#{count1} {book.__str__()}"
                    print(str)
                    count1 += 1
            elif user1 == 2:
                print('\n====== Rented ======\n')
                count1 = 1
                for book in r_books:
                    str = f"Book#{count1} {book.__str__()}"
                    print(str)
                    count1 += 1
            elif user1 == 3:
                print('\n====== Audio ======\n')
                count1 = 1
                for book in a_books:
                    str = f"Book#{count1} {book.__str__()}"
                    print(str)
                    count1 += 1
            elif user1 == 4:
                print('\n====== Paper ======\n')
                count1 = 1
                for book in p_books:
                    str = f"Book#{count1} {book.__str__()}"
                    print(str)
                    count1 += 1
        elif user == 2:
            print('\n====== Rent/Return ======\n')
            print('Select Option: (1) Rent (2) Return')
            user1 = int(input('User input: '))
            if user1 == 1:
                print('\n====== Rent ======\n')
                print('\nAvailable Books to rent\n')
                count = 1
                for book in nr_books:
                    str = (f'({count}) Book ID: {book.book_id} \ '
                           f'Title: {book.title}')
                    print(str)
                    count += 1
                change = 0
                user2 = int(input("Enter Book ID: "))
                for book1 in nr_books:
                    if book1.book_id == user2:
                        rent_book(nr_books, r_books, book1)
                        if book1 in r_books:
                            print(f'You have rented {book1.title}'
                                  f'with Book ID#{book1.book_id}')
                        change += 1
                    if change >= 1:
                        pass
            elif user1 == 2:
                print('\n====== Return ======\n')
                print('\n====== Rented Books ======')
                count = 1
                for book in r_books:
                    str = (f'({count}) Book ID: {book.book_id} \ '
                          f'Title: {book.title}')
                    print(str)
                    count += 1
                user2 = int(input("Enter Book ID: "))
                for book1 in r_books:
                    if book1.book_id == user2:
                        return_book(nr_books, r_books, book1)
                        if book1 in nr_books:
                            print(f'You have returned {book1.title}'
                                  f'with Book ID#{book1.book_id}')
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

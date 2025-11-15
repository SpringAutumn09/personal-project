
class Books():
    due_date_time = 10
    def __init__(self, title, author, genre, isbn, available_copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.available_copies = available_copies
        self.due_date = None  # None means not borrowed yet    
    def DisplayBookInfo(self):
        print(f""" Author: {self.title}
                    Genre: {self.genre}
                    ISBN: {self.isbn}
              """)
    def CheckAvailablity(self):
        if self.available_copies > 0:
                
            print(f"Avaiblable copies: {self.available_copies}")
        else:
            if self.due_date != None:
                print(f"There isn't {self.title} book in the library at the moment but the due date of the lended copie is {self.due_date}")
            else:
                print(f"There isn't any copie this book available or lended at the library")


class Library():
    def __init__(self, list_of_books, list_of_patrons):
        self.list_of_books = list(list_of_books)
        self.list_of_patrons = list(list_of_patrons)

    def Search(self, book):
        if book in self.list_of_books:
            return True
    
    def AddBooks(self, title, author, genre, isbn, available_copies):
        if title in self.list_of_books:
            title.available_copies += 1
        else:    
            title = Books(title, author, genre, isbn, available_copies)
            self.list_of_books.append(title)
        
    
    def RemoveBook(self, book):
        if book in self.list_of_books:    
            self.list_of_books.remove(book)
        else:
            print("There is no such book in the library to be deleted.")    
    def RegisterPatron(self, name, id, borrowed_books, late_fee_balance):
        if name in self.list_of_patrons:
            print("Person with this identity is already registered")
        else:
            name = Patron(name, id, [], 0)
            self.list_of_patrons.append(name)
    
    def UnregisterPatron(self, patron):
        if patron in self.list_of_patrons:
            self.list_of_patrons.remove(patron)
        else:
            print("There is no patron with given identity to be unregistered")

class Patron():
    late_fee_per_day = 3
    def __init__(self, name, id, borrowed_books, late_fee_balance):
        self.name = name
        self.id = id
        self.borrowed_books = list(borrowed_books)
        self.late_fee_balance = late_fee_balance

    def Borrowbook(self, patron_name, library_name, title):
        if library_name.Search(title) == True:
            if title.available_copies != 0:
                title.due_date = title.due_date_time
                title.available_copies -= 1
                patron_name.borrowed_books.append(title)
            else:
                print("The book is currently lent.")
        else:
            print("There isn't such book in the library.")
    
    def ReturnBook(self, patron_name, library_name, title):
        if library_name.Search(title) == True:
            title.available_copies += 1
            if title.due_date < 0:
                patron_name.late_fee_balance += abs(title.due_date)*patron_name.late_fee_per_day
                title.due_date = 0
            else:
                title.due_date = 0
        else:
            print("There has been a mistake, The library doesn't own such book nor lent it before")
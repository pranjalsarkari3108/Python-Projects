class Library:
    def __init__(self, list_books, library_name):
        self.list_books = list_books
        self.lend_books = {}
        self.library_name = library_name
        for i in self.list_books:
            self.lend_books[i] = None

            
    def add_book(self, book):
        self.list_books.append(book)
        self.lend_books[book] = None


    def lend_book(self, book, lender):
        if book in self.list_books:
            if self.lend_books[book] == None:
                self.lend_books[book] = lender
            else:
                print(f"Sorry {self.lend_books[book]} has borrowed the book")

        else:
            print("Required book is not availbale")
    def return_book(self, book):
        if book in self.list_books:
            if self.lend_books[book] != None:
                self.lend_books[book] = None
            else:
                print("This book has borrowed by nobody")
        else:
            print(f"This book is not in {self.library_name} library")
    def display_books(self):
        for i, j in self.lend_books.items():
            print(f"{i} borrowed by {j}")
def main():
    Hindutwa = Library(['Ramayan', 'Geeta', 'Mahabharat', 'Satyarth Prakash', 'Ved'], 'Sanatan')
    a = True
    while(a):
        print(f"Welcome to {Hindutwa.library_name} Library. Here 1 for add_book, 2 for lend_book, 3 for return_book and 4 for display_books otherwise exit");
        print("Enter your choice")
        b = int(input())
        if b == 1:
            print("Enter The book name")
            book = input()
            Hindutwa.add_book(book)
        elif b == 2:
            print("Enter the book name and borrower name")
            book = input()
            lender = input()
            Hindutwa.lend_book(book, lender)
        elif b == 3:
            print("Enter the book name")
            book = input()
            Hindutwa.return_book(book)
        elif b == 4:
            Hindutwa.display_books()
        else:
            a = False
            continue
if __name__ == '__main__':
    main()
    
        

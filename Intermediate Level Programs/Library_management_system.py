class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Books Currently Present in LIBRARY {self.name} are : \n")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("\nDatabase has been UPDATED !! Now You can Take this BOOK $$")
        else:
            print(f"Book is already has taken by :  {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("\nDone !! Book has been added to the Book List\n")

    def returnBook(self, book):
        self.lendDict.pop(book)
        print("\nDone !! Your Book has been Successfully Returned !! \n")

if __name__ == '__main__':
    satyam = Library(['Python Tutorials For Absolute Beginners', 'Let us C', 'Complete github Tutorial', 'C++ Basics', 'C# Basics'], "@Satyam Tripathi & Company")

    while(True):
        print(f"\n\n\t\t\tWelcome to the {satyam.name} Library \n\n Please Enter your choice to continue : \n")
        print("1. Add Book To The Library")
        print("2. Issue a Book")
        print("3. Display All The Books")
        print("4. Return a Book")
        choice = input()
        if choice not in ['1','2','3','4']:
            print("Warning !! Please Enter a valid Option !!")
            continue

        else:
            choice = int(choice)


        if choice == 3:
            satyam.displayBooks()

        elif choice == 2:
            book = input("Please Enter the name of the book you want to ISSUE:")
            if book not in satyam.booksList:
                print("Warning !! Book Not Found in the our BOOKLIST !!")
            else:
             user = input("Please Enter your Name : ")
             satyam.lendBook(user, book)

        elif choice == 1:
            book = input("Please Enter the name of the Book you want to ADD : ")
            satyam.addBook(book)

        elif choice == 4:
            book = input("\nEnter the name of the book you want to return : ")
            satyam.returnBook(book)

        else:
            print("Warning !! Invalid Option !!")

        print("\n\nDo You want to CONTINUE !! Press[y/n] : ")
        cho = input()
        cho=cho.lower()
        if cho == "n":
            exit()
        elif cho == "y":
            continue


class Library:
    def __init__(self,list,name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(F"we have following books in library : {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self,user,book):
        if  book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender - Book batabase has been updated. you can take the book now ")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)
        #pop - remove and update the dictionary


if __name__ == '__main__':
    ansh = Library(['python','Rich Daddy Poor Daddy','Harry Potter','C++ Basic','Algorithms by CLRS'],"ROYAL_FOUDATION")

    while(True):
        print(f"welcome to the {ansh.name} Library. Enter your choice to continue ")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book\n")
        # print(type(ansh))

        user_choice = (input())
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            ansh.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you wnat to lend : ")
            user = input("Enter your name : ")
            if book in ansh.booksList:
                """ 
                 dir() tries to return a list of calid attributes of the object. if the object had __dir__() method,
                 the nethos will be called and must return the list of attributes. if the object doesn't have __dir__()
                 method, this method tries to find information from the __dict__ attribute (if defined), and from type object.
                """
                ansh.lendBook(user,book)
            else:
                print(f"{book} is not in our Library")

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            ansh.addBook(book)
            print(f"you give {book}")

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return : ")
            ansh.returnBook(book)
            print(f"please give the review this book (range 1 to 5)")
            x =  int(input())
            print(f"{book} book review is {x}. 💕 thank you 💕")
        else:
            print("not a valid option")

        print("Press q to quit and c to continue")
        user_choice = ""
        while(user_choice != "c" and user_choice!="q"):
            user_choice = input()
            if user_choice == 'q':
                exit()
            elif user_choice == 'c':
                continue
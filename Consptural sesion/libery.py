class Book:
    def __init__(self,id,name,quantity) -> None:
        self.id=id
        self.name=name
        self.quantity=quantity
class User:
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.password=password
        self.name=name
        self.borrowedBooks=[]
        self.returnBooks=[]


class LIbrary:
    def __init__(self,name) -> None:
        self.name=name
        self.users=[]
        self.Books=[]
        
    def addBook(self,id,name,quantity):
        book=Book(id,name,quantity)
        self.Books.append(book)
        print(f'{book.name} add book success full')

    def addUser(self,id,name,password):
        book=User(id,name,password)
        self.users.append(book)
        return book


bsk=LIbrary("bishwa shahitja kendro")
admin=bsk.addUser(1000,"admin",'admin')
ratn=bsk.addUser(17,'ratin','123')
cpBook=bsk.addBook(11,'pbook',5)


currentUser=admin
while True:
    if currentUser==None:
        print("No lggen in ser \n")

        option=input("Login or Register (L\R)")

        if option == "L":
            id=int(input("Enter Id:"))
            password=input("Enter password")
            match=False
            for user in bsk.users:
                if user.id==id and user.password==password:
                  currentUser=user
                  match=True
                  break
                if match ==False:
                    print("No usr Found !\n")
        elif option == "R":
            id=int(input("Enter your id"))
            name=input("Enter your name")
            password=input("Enter your password")
            for user in bsk.users:
                if usr.id ==id:
                    print("usr alreay exits")

            user=bsk.addUser(id,name,password)
            currentUser=user
    else:
        print(f"Wlcome back{currentUser.name} !\n")
        if currentUser.name=="admin":
            print("options:\n")
            print("1:Add book ")
            print("1:Add user ")
            print("1:Add all books ")
            print("1:Add Logout ")

            ch=int (input("Enter"))
            if ch==1:
                id=int(input("Enter your id"))
                name=input("Enter book name")
                quantity=input("Enter No of book")

                bsk.addBook(id,name,quantity)
            elif ch==3:
                for book in bsk.Books:
                    print(f'{book.id}\t{book.name}\t{book.quantity}')
                print('\n')
            elif ch==4:
                currentUser=None


class Start_cinema:
    hall_list= []
    def entry_hall(self,rows,cols,hall):
        hall=Hall(rows,cols,hall)
        self.hall_list.append(hall)


class Hall:
    show_list=()
    seats={}

    def __init__(self,rows,cols,hall) -> None:
        self.rows=rows
        self.cols=cols
        self.hall_no=hall
        self.seat = [[0] * cols for _ in range(rows)]
       
    
    def entry_show(self,id,movie_name,time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        self.rt=(f'id:{self.id} movie_name :{self.movie_name} time: {self.time}' ,)
        self.show_list +=self.rt
        self.seats.update({id:self.seat})
    
    def book_seats(self,id,quantity):
        
            for key,seat in self.seats.items():
                
                if(id == key):
                    for q in range(0,quantity):
                        row=int(input("Enter your seat row")) 
                        col=int(input("Enter your seat col")) 
                        if self.rows>=row and self.cols>=col:

                            if(seat[row][col] == "Booking"):
                                print("you can't booking this seat")
                            else:
                                seat[row][col] = "Booking"
                                print("your booking is completed")
                        else:
                            print("your seat don't exist this hall room")
                    break
                else:
                
                    print("This movies is not available this time")
                    break


                
    def view_show_list(self):
        for item in self.show_list:
            print(item)
    
    def view_available_seats(self,id):
        if id in self.seats:
            for row in self.seats[id]:
                print(row)
        else:
            print("please Enter right id and try again")


    def __repr__(self) -> str:
        return f'show_list:{self.show_list} seats:{self.seats}'

cineplex=Start_cinema()
sk=Hall(5,5,1)
mk=Hall(10,10,2)
sk.entry_show(111,'jayan',"10/2/2024")
sk.entry_show(112,'number one',"10/2/2024")
sk.entry_show(113,'sprider man',"10/2/2024")
sk.entry_show(114,'pokemon',"10/2/2024")
mk.entry_show(111,'abatar',"10/2/2024")
mk.entry_show(112,'naruto',"10/2/2024")
mk.entry_show(113,'black_cover',"10/2/2024")
mk.entry_show(114,'demonsh_slyer',"10/2/2024")

loop_controler=True
while loop_controler:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEAS")
    print("3. BOOK TICKET")
    print("4. EXit")
    option=int(input("Enter OPTION:"))
    if(option==1):
       mk.view_show_list()
       print("\n\n")
    elif(option ==2):
        id=int(input("Enter id:"))
        mk.view_available_seats(id)
        print("\n\n")
    elif(option ==3):
        id=int(input("Enter id:"))
        qu =int(input("Enter quantity:"))
        mk.book_seats(id,qu)
         
    elif(option==4):
        break
    else:
        print("please Enter you right number")
    
    




from Company import Company,Product
from User import Seller,Customer
sakib = Company('sk')
def main(login_system):
    
    while True:
        print("Press 1 for  sign up As a Customer")
        print("press 2 for sign up As a seller")
        print("Press 3 for Login")
        
        controller = int(input("-->"))

        if controller ==1:
            email = input("Enter your Email")
            password= input("Enter your password")
            new_customer = Customer('None',email,password)
            sakib.add_customer(new_customer)
            login_system()
        elif controller ==2:
            email = input("Enter your Email")
            password= input("Enter your password")
            new_seller = Seller('None',email,password)
            print(new_seller)
            sakib.add_seller(new_seller)
            login_system()
        elif controller ==3:
            login_system()
        else :
            print("Please Enter your right number you no another choice")


@main
def login_system():
    print("press login")
    print("press 1 for customer")
    print("press 2 for seller")

    login_controller = int(input("--->"))
    if login_controller == 1:
        email = input("Enter your Email")
        password= input("Enter your password")
        for customer in sakib.Customer_list:
            if customer.email == email and customer.password == password:
                for sk in sakib.product_list:
                    print(f'item_name{sk.name} and it price {sk.price}')
                
    elif login_controller ==2:
        email = input("Enter your Email")
        password= input("Enter your password")
        for seller in sakib.Seller_list:
            if seller.email == email and seller.password == password:
                con=int(input("press 1 for add products \n press 2 for main page"))
                if con == 1:
                    name = input("Enter your name")
                    price = input("Enter product price")
                    quantity = input("Enter product Quantity")
                    product =Product(name,price,quantity)
                    sakib.add_product(product)
                else:
                    pass
            else:
                pass
    else:
        print("Please Enter your right number you no another choice")


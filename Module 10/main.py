from Menu import Pizza,Burger,Menu,Drinks
from Restaurant import Restaurant
from User import Chef,Customer,Server,Manager
from Order import Order
def main():
    menu = Menu()
    Pizza_1 = Pizza('shutki pizza',600,'large',["shutki,'onion"])
    menu.add_menu_item('pizza',Pizza_1)
    Pizza_2 = Pizza('Alur Vrota pizza',400,'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',Pizza_2)
    Pizza_3 = Pizza('Dal pizza',500,'large',['dal','oil'])
    menu.add_menu_item('pizza',Pizza_3)


    # addd burger 
    burger_1 = Burger('Naga Burger',1000,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger',1200,'chicken',['goro','hadi'])
    menu.add_menu_item('burger',burger_2)



    # add drink to the menu

    coke = Drinks ('coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha',300,False)
    menu.add_menu_item('drinks',coffee)


    # menu.show_menu()

     # star  restaurant 
    restaurant = Restaurant("sai_baba_Restaurant",2000, menu)
    # employees
    manger =Manager('kala chan Manager',5,'kala@chan.cm','kalapur',1500,'1/5/2023','core')
    restaurant.add_employee('manager',manger)

    Chf =Chef("Rustmom baburchi",6,'chuapr@.com','rustmangera',3500,'fre,1,2023','chf','pizza')
    restaurant.add_employee('chef',Chf)


    server = Server('kamal',545,'@','jam',15,"23/2/2003",'serve')
    restaurant.add_employee("server",server)

    restaurant.show_employees()



    # add customer

    customer_1 =Customer("sakib khan",6,'king@khan.com',"banali",10000)
    order_1 =Order(customer_1,[Pizza_1,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    restaurant.received_payment(order_1,2000,customer_1)
    print('revenve and balance after first customer ',restaurant.revenue,restaurant.balance)



    customer_2 =Customer("sakib al hasan",6,'king@khan.com',"banali",10000)
    order_2 =Order(customer_2,[Pizza_2,coke])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    restaurant.received_payment(order_1,2000,customer_2)
    print('revenve and balance after second customer ',restaurant.revenue,restaurant.balance)




    restaurant.pay_expense(restaurant.rent,'Rent')
    print('after rent',restaurant.revenue, restaurant.balance ,restaurant.expense)
    

if __name__ == '__main__':
    main()
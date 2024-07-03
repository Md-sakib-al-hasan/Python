class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quantiy):
        product= {'item': item,"price":price,"quantity":quantiy}
        self.cart.append(product)
    def remove (self,item):
         for items in self.cart:
             if( items['item'] == item):
                 self.cart.remove(items)
        
    def checkout(self,amount):
        total=0
        for element in self.cart:
            total+=element['price']*element['quantity']
        if total <=amount:
            print("you can buy")
        else:
            print('you cant byt')

swapan = Shopping('Alan Swapon')
swapan.add_to_cart('alu',50,6)
swapan.add_to_cart('dim',12,24)
swapan.add_to_cart('rice',50,5)
swapan.checkout(10)
swapan.remove('alu')
print(swapan.cart)

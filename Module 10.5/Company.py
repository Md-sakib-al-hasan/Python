
class Company:
    def __init__(self,name) -> None:
        self.name =name
        self.Seller_list=[]
        self.Customer_list=[]
        self.product_list=[]
    def add_seller(self,seller):
        self.Seller_list.append(seller)
    def add_customer(self,customer):
        self.Customer_list.append(customer)
    def add_product(self,product):
        self.product_list.append(product)


class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name=name
        self.price =price
        self.quantity=quantity
        

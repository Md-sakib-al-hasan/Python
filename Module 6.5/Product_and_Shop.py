class Product:
    cart=[]
    def __init__(self,name,price,brand,types) -> None:
        self.name=name
        self.price=price
        self.brand=brand
        self.type=type
        
    
    def __repr__(self) -> str:
        return f'product name {self.name}.this product price {self.price}.this is {self.brand}.it create by {self.brand}'
class Shop(Product):
    def __init__(self,name,price,brand,types) -> None:
        super().__init__(name,price,brand,types)

    def add_product(self,item,brand,price):
        product={'item':item,'brand':brand,'price':price}
        self.cart.append(product)
    def cheak(self,item):
        for i in self.cart:
            if(i['item'] ==item ):
                print('yes')
                break
            if(i['item'] !=item and i==self.cart[-1]):
                print('no')

        
    def __repr__(self) -> str:
        return f'item name {self.item} its price {self.price} and ist brand'


sakib=Product('chip',5,'pran','food')
watch=Shop('sakib',78,'man','it')
watch.add_product('alu','sk',45)
watch.add_product('watch','iphone',4500)
watch.add_product('computer','asa',787)
watch.add_product('rice','ispahani',78)
watch.cheak('man')
print(sakib.cart)
print(watch.name)

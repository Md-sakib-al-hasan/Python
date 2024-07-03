class Shop:
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart=[]
    def add_to_cart(self,item):
        self.cart.append(item)


mehjabeen=Shop('mez jab een')
mehjabeen.add_to_cart('shoe')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('nisho')
nisho.add_to_cart('hat')
nisho.add_to_cart('wtach')
print(nisho.cart)
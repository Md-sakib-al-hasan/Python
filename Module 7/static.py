class Shopping:
    cart = []
    origin='china'
    def __init__(self,name,location) -> None:
        self.name = 'jamu na ciyt'
        self.location='jam er maj khane'
    def purchase (self,item,price,amount):
        remaining =amount -  price
        print(f'buying: {item} for price :{price} and {remaining}')

    @staticmethod
    def mul(a,b):
        print(a*b)

    @classmethod
    def check(self,item):
        print('hodey dekho')



Shopping.check('sk')
Shopping.mul(10,20)        
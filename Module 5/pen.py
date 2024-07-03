class Pen:
    manufactured = 'Bangladesh'
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

my_pen=Pen('kamal','matador',5)
her_pen=Pen('Rahol','item',11)
old_pen=Pen('tanha','tan',80)
print(my_pen.owner,my_pen.brand,my_pen.price)
print(her_pen.owner,her_pen.brand,her_pen.price)
print(old_pen.owner,old_pen.brand,old_pen.price)

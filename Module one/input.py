# money = input('give me some money : ')
# print(money)
# print(type(money))
from decimal import Decimal;
first_money = Decimal( input("give me some money"))
second_money = Decimal(input("give me some money"))
print(first_money+second_money)

x = Decimal('0.1')
y = Decimal('0.2')
print(type(x))
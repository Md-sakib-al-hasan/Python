class Person:
    def __init__(self,name,age,height,wight) -> None:
        self.name = name
        self.age=age
        self.height=height
        self.wight=wight
    def eat (self):
        print('vat mangso polau korma')
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, wight,team) -> None:
        self.team=team
        super().__init__(name, age, height, wight)
    def __add__(self,other):
        return self.age + other.age
    def __gt__(self,other):
        return self.age > other.age

    def eat (self):
        print('vegetables')
    def exercise():
        print('poy dinya taka nosto')

sakib=Cricketer('sakib',38,68,91,"BD")
moshi=Cricketer('moshi',78,7,80,'BD')

print(sakib +moshi)
print(sakib <moshi)
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('ha na na eating bannana')
    def move (self):
        pass
class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagori = 'Monkey'
        self.name=name
        super().__init__()
    def eat(self):
        return super().eat()

layka = Monkey('lucky')
layka.eat()
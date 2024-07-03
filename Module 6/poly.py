class Animal:
    def __init__(self,name) -> None:
        self.name=name

    def make_sound(self):
        print('animl making some sound')

class Cat (Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

don =Cat('real Don')
don.make_sound()

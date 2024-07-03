
class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price = price
        self.color=color
        self.origin=origin
    def run(self):
        return f'Running laptop: {self.brand}'

class Laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory
        self.ssd=ssd
    def run(self):
        return f'Running laptop: {self.brand}'
    def coding (self):
        return f'learning python and praticing'
    


class Phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,origin)
    def run (self):
        return f'phoe tipa tipi kore'
    def phone_call (self,number,text):
        return f'Sending to SMS to :{number} with: {text}'
    def __repr__(self) -> str:
        return f'phone:{self.brand}{self.price} {self.dual_sim}'



class Camera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel
    def run(self):
        pass
    def change_lens(self):
        pass

my_phone = Phone('iphone',12000,'silver','china',True)
print(my_phone.brand)
print(my_phone)
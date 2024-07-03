from abc import ABC,abstractmethod
class Restaurant:
    def __init__(self,restaurant_name,location,restaurant_registration_number) -> None:
        self.restaurant_name=restaurant_name
        self.location=location
        self.restaurant_registration_number=restaurant_registration_number
        self.owner_list=[]

class Owner(ABC):
    def __init__(self,name,type_of_job) -> None:
        self.name=name
        self.type_of_job=type_of_job
    
    @abstractmethod
    def __repr__(self) -> str:
        return {'name':self.name,'type_of_job':self.type_of_job}
    

class Customer():
    def __init__(self,name,money) -> None:
        self.name=name
        self.money=money

    def add_money(self,money):
        self.money=self.money+money
    def buy_item(self,*args):
        #TODO someting
        pass
    


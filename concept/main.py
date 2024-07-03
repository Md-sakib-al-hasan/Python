from abc import ABC,abstractmethod
class Ride_sharing:
    def __init__(self,company_name,) -> None:
        self.company_name=company_name
        self.riders=[]
        self.drivers =[]

    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"{self.company_name} has {len(self.riders)} riders and {len(self.drivers)} Drivers"


class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name 
        self.email = email
        self.nid = nid

    @abstractmethod
    def display_profile():
        raise NotImplementedError
    

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.wallet = 0 
        self.current_location = current_location

    def __repr__(self) -> str:
        return f'Driver name {self.name} and mail is {self.email}'

class Rider(User):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_location =current_location
        super().__init__(name, email, nid)

    def __repr__(self) -> str:
        return f'Rider name {self.name} and mail is {self.email}'

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location =start_location
        self.end_location  = end_location
        self.driver =None
        self.rider = None

    def start_rider(self):
        pass
    def end_rider(self):
        pass
    def __repr__(self) -> str:
        return f"start from {self.start_location} to {self.end_location}"

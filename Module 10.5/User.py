
class User:
    def __init__(self,name,email,password) -> None:
        self.name =name
        self.email=email
        self.password=password

class Customer(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)


class Seller(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)


        
class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw=100
        self.max_withdraw=1000000
    def get_blance(self):
        return self.balance
    def deposit(self,amount):
        if amount > 0:
            self.balance +=amount
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print( f'fokira. you can widthdraw below {self.min_withdraw}')
        
        elif amount > self.max_withdraw:
            print( f'bank fokir hoye jabe. you cna not with more than {self.max_withdraw}')
        else:
            self.balance -=amount
            print( f'here is your money {amount}')
            print(f'your current balance{self.get_blance()}')



brack = Bank(15000)
brack.withdraw(25)
brack.withdraw(250000000000000000)
brack.withdraw(1000)
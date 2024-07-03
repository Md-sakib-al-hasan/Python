class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name
        self._brance = 'jumgora'
        self.__balance=initial_deposit
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
    def widthraw(self,amount):
        if amount <self.__balance:
            self.__balance =self.__balance-amount
            return amount
        else:
            return f'forkia tak nai'
rafsun= Bank ('chooto bor',10000)
print(rafsun.holder_name)
rafsun.deposit(40000)
print(rafsun.get_balance())
print(dir(rafsun))
class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name = name
        self.orders =[]
        self.chef = None
        self.server = None
        self.manager = None
        self.rent =rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance =0
        self.profit =0


    def add_employee(self,employee_type,employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server =employee

        elif employee_type == 'manager':
            self.manager =employee

    def add_order(self,order):
        self.orders.append(order)

    def received_payment(self,order,amount,customer):
        if  amount >= order.bill :
            self.revenue +=order.bill
            self.balance +=order.bill
            customer.due_amount =0
            return amount - order.bill 
    
    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense +=amount
            self.balance -=amount
            print(f'Expense {amount} for{description}')

        else:
            print(f'Not enough money to pay {amount}')
    
    def pay_salary (self,employee):
        if employee.salary < self.balance:
            employee.receive_salary()
        
    def show_employees(self):
        print("showing employee")
        if self.chef is not None:
            print(f'chef: {self.chef.name} with salary {self.chef.salary}')
        if self.server is not None:
            print(f'server: {self.server.name} with salary {self.chef.salary}')
        if self.manager is not None:
            print(f'manager: {self.manager.name} with salary {self.chef.salary}')
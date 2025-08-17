class MinimumBalanceError(Exception): 
    pass

class Account:
    AccNumber = 1001
    
    def __init__(self, name, balance):
        if balance < 1000: 
            raise MinimumBalanceError
        self.name = name
        self.balance = balance
        self.acc_number = Account.AccNumber
        Account.AccNumber += 1
    
    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance - amt < 1000:
            raise MinimumBalanceError
        self.balance -= amt

    def show_details(self):
        print("Name:", self.name)
        print("Account number:", self.acc_number)
        print("Balance:", self.balance)

try:
    a1 = Account('Swarali', 2000)
    a1.deposit(1000)
    a1.withdraw(2500)
    a1.show_details()
except:
    print("Minimum balance must be 1000")

print(' ')
a2 = Account('Swarali_A', 3000)
a2.show_details()
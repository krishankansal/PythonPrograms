import sys
class Customer:
    'customer class with bank related operations'
    # static variable
    bank_name = 'kkkbank'

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance = self.balance + amount
        print("After deposit balance is: ",self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds.. cannot perform this operation")
            sys.exit()
        else:
            self.balance = self.balance - amount
        
        print('After withdraw the balance is', self.balance)

print("Welcome to", Customer.bank_name)
name = input('Enter your name')
c = Customer(name)
while True:
    print('d-Deposit\nw-withdraw\ne-exit')
    option=input("Choose your Options:")
    if option.lower() == 'd':
        amt=float(input('Enter the amount to deposit:'))
        c.deposit(amt)
    elif option =='w' or option == 'W':
        amt=float(input("Enter amount to withdraw"))
        c.withdraw(amt)
    elif option =='e' or option =='E':
        print('Thanks for banking')
        sys.exit()
    else:
        print('choose valid option')




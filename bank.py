"""
Create Account Class with two attributes - balance and account no.
Create methods for debit,credit and printing balance
"""


class Account:
    def __init__(self, acc_no, pin, balance):
        self.balance = balance
        self.acc_no = acc_no
        self.pin = pin

    def Print_balance(self):
        print("current Balance:",self.balance)

    def debit(self, acc_no, pin, amount):
        self.Print_balance()
        if self.acc_no != acc_no or self.pin != pin:
            print("Incorrect acc_no or pin")
        elif amount > self.balance:
            print("insufficient amount")
        else:
            self.balance -= amount
            print("Amount debited:",amount)
            self.Print_balance()

    def credit(self, acc_no, pin, amount):
        self.Print_balance()
        if self.acc_no != acc_no or self.pin != pin:
            print("Incorrect acc_no or pin")
        else:
            self.balance += amount
            print("Amount credited:",amount)
            self.Print_balance()


p1 = Account(acc_no=1234, pin=4321, balance=5000)
p1.debit(acc_no=1234,pin=4321,amount=3000) #valid case

p1.debit(acc_no=124,pin=4321,amount=3000) #invalid case

p1.debit(acc_no=1234,pin=4321,amount=6000) #ivalid case

p1.credit(acc_no=1234,pin=4321,amount=3000) #valid case

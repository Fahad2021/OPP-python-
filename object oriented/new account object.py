class BankAccount:
    def __init__(self):
        self.balance=0

    def deposite(self, amount):  # method/function
            self.balance += amount
            print("Deposite:",self.balance)

    def withdraw(self,amount):      #method/function
        self.balance-=amount
        if self.balance<0:
             print("your account is empty!!!")
        else:
         print("current Balance:",self.balance)




a=BankAccount()
a.deposite(20000)
a.withdraw(9000)

b=BankAccount()
b.deposite(2000)
b.withdraw(345)






# class BankAccount:
#     def __init__(self):
#         self.balance=0
#
#     def deposite(self, amount):  # method/function
#             self.balance += amount
#             print("Deposite:",self.balance)
#
#     def withdraw(self,amount):      #method/function
#         self.balance-=amount
#         if self.balance<0:
#              print("your account is empty!!!")
#         else:
#          print("current Balance:",self.balance)
#
#
#
#
# a=BankAccount()
# a.deposite(20000)
# a.withdraw(9000)
#
# b=BankAccount()
# b.deposite(2000)
# b.withdraw(345)
#
#
#
#
#
# class BankAc:
#     def __init__(self):
#          self.balance=0
#     def deposite(self,ammount):
#        self.balance+=ammount


#     def withdraw(self,ammount):
#         if self.balance>=ammount:
#           self.balance-=ammount
#           print(self.balance)
#         else:
#            print("Insuffint balance",self.balance)

# def current_balance(self):
#     return self.balance

# a=BankAc()
# a.deposite(1000)
# a.withdraw(500)
# print(current_balance)


blnc=0
def depo(amount):
  global blnc
  blnc=blnc+amount
  return blnc
def withd(amount):
  global blnc
  blnc=blnc-amount
  return amount

def current_blnc():
  return blnc

print("you deposite",depo(400))
print("you withdraw",withd(200))
print("you current balance",current_blnc())




class CreditCard:
    def __init__(self,customer,bank,acount,limit):
        self._customer=customer
        self._bank=bank
        self._account=acount
        self._limit=limit
        self._balance=0
    def get_customer(self):
        print(self._customer)
    def get_bank(self):
        print (self._bank)
    def get_acount(self):
        print( self._account)
    def get_limit(self):
        print (self._limit)
    def get_balance(self):
        print ("Your Current Balance is:",self._balance)
    def charge(self,price):
        if price+self._balance>self._limit:
            print("Your acount is empty")
        else:
            self._balance+=price
            print("You have Some Money")
    def make_payment(self,amount):
        self._balance-=amount

b=CreditCard("Fahad","Islami Bank M Cash",12345,10000)
b.get_customer()
b.get_bank()
b.get_balance()
b.make_payment(50000)
b.charge(20)
# a=CreditCard("Bonna","Grammen Bank",23452,10000)
# a.get_customer()
# a.get_bank()
# a.get_balance()
# a.charge(177)

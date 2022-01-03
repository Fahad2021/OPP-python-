# class Resturent:
#     name=''
#     owner=''

#     def details(self):
#         print(self.name,self.owner)
    
#     def address_details(self):
#         print(self.name,self.owner,self.address)

# res1=Resturent()
# res1.name="fahad dhoi ghor"
# res1.owner="fahad"
# res1.address="khirati,kapasia,gazipur"

# res1.address_details()
def trac(f):
    def g(x):
        print(f.__name__,x)
        value=f(x)
        print('return'), 
        repr(value)
        rteurn 
        value
    return g
fib=trac(fib)
print(fib(3))
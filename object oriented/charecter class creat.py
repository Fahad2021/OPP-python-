class shop:
    vat=1.5
    def __init__(self,pant,shirt,mbl):
        self.pant=pant
        self.shirt=shirt
        self.mbl=mbl

    def finalprice(self):
        self.pant=self.pant*self.vat
        self.shirt=self.shirt*self.vat
        self.mbl=self.mbl*self.vat

    
fshop=shop(1000,1000,5000)
print(fshop.__dict__)
print(fshop.pant,fshop.shirt,fshop.mbl)
fshop.finalprice()
print(fshop.__dict__)


        
        

    
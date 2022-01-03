class Miu:
    name=""
    roll=""

N=Miu()
N.name="rahim"
N.roll=678

M=Miu()
M.name="karim"
M.roll=679

O=Miu()
print(isinstance(O,Miu))
O.name="tah"
O.roll=650

print(f"Student Information:Name:{N.name},Roll:{N.roll}")
print(f"Student Information:Name:{M.name},Roll:{M.roll}")
print(f"Student Information:Name:{O.name},Roll:{O.roll}")

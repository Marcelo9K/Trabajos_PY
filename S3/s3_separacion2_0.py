import random as rd
Vmayor=[]
Vmenor=[]
for i in range (10):
    num=rd.randint(1,10)
    if num >= 5:
        Vmayor.append(num)
    else:
        Vmenor.append(num)
print(Vmayor)
print(Vmenor)
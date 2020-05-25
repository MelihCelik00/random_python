import math
import time
a = 6378137.0000 # m
b = 6356752.3141 # m

e = (((a**2)-(b**2))/(a**2))**(1/2)

E_zero = -2.5
M = -2.5
Ek = 0
k = 0

while True:
    if k==0:
        print(E_zero)
        a = E_zero
        k += 1

    if k==1:
        print("Ustteki iften cikti")

    Ek = M + e * math.sin(a)

    print("Ek: ",Ek," E(k-1): ",a)
    #time.sleep(1)

    
    if(Ek == a):

        print("It is equal")
        break

    a = Ek

print("It is equal finally!")

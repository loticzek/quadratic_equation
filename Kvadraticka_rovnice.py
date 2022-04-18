print("Program na výpočet kvadratické rovnice")
print("Tvar rovnice: ax^2+bx+c=0")
a = int(input("Zadej koeficient a: "))
b = int(input("Zadej koeficient b: "))
c = int(input("Zadej koeficient c: "))
d = b*b - 4 * a * c
x1 = ((b * -1) + (d**(1/2))) / (2 * a)
x2 = ((b * -1) - (d**(1/2))) / (2 * a)
if d > 0:
    print("Kořen x1: ", x1)
    print("Kořen x2: ", x2)
elif d < 0:
    print("rovnice NEMÁ v reálných číslech řešení")
elif d == 0:
    print("rovnice má jeden, dvojnásobný kořen: ", x1)
input()



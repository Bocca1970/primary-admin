
# --------------- Python 21 ---------------
# --------------- Kalkulator --------------

import math

def sabiranje(x, y):
   return x + y

def oduzimanje(x, y):
   return x - y

def mnozenje(x, y):
   return x * y

def deljenje(x, y):
   return x / y

def eksponencija(x, y):
    return x ** y

print("Izaberite jednu od sledecih operacija")
print('\r')
print("1. Sabiranje")
print("2. Oduzimanje")
print("3. Mnozenje")
print("4. Deljenje")
print("5. Eksponencija")
print('\r')

opcija = input("Unesite opciju (1) (2) (3) (4) ili (5): ")
print('\r')

broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))
print('\r')

if opcija == '1':
   print(broj1,"+",broj2,"=", sabiranje(broj1,broj2))

elif opcija == '2':
   print(broj1,"-",broj2,"=", oduzimanje(broj1,broj2))

elif opcija == '3':
   print(broj1,"*",broj2,"=", mnozenje(broj1,broj2))

elif opcija == '4':
   print(broj1,"/",broj2,"=", deljenje(broj1,broj2))

elif opcija == '5':
    print(broj1,"na",broj2,"=", eksponencija(broj1,broj2))
else:
   print("Pogresan unos")
   

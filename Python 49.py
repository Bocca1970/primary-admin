
# --------------- Python 49 ----------------
# Izracunavanje povecanja/smanjenja cena u %

# Povecanje cena u % = 100*(Nova cena-Stara cena)/Stara cena
# Smanjenje cena u % = 100*(Stara cena-Nova cena)/Stara cena

print("Izaberite jednu od sledecih opcija")
print('\r')

print("1. Povecanje cena")
print("2. Smanjenje cena")
print('\r')

opcija = input("Unesite opciju (1) ili (2): ")
print('\r')

a = float(input("Stara cena: "))
b = float(input("Nova cena: "))


def procenat(a, b):
    if (a<=0 or b<=0):
        return 0
    else:
        pass

    povecanje = ((b-a)/a*100)
    smanjenje = ((a-b)/a*100)

    if opcija == '1':
        print("Povecanje cene iznosi ", povecanje, '%')
    elif opcija =='2':
        print("Smanjenje cene iznosi ", smanjenje, '%')
    else:
        print("Pogresan unos!")
        
procenat(a, b)
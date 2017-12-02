
# --------------- Python 28 ---------------
# -------- Odnos telesna masa/visina ------


# Izracunajte da li vasa telesna masa odgovara vasoj telesnoj visini

s = str(input("Ime i prezime: "))
t = float(input("Tezina u kg: "))
v = int(input("Visina u cm: "))

odnos = t / ((v/100) ** 2)

print("Ime i prezime: ", s)
print("Tezina u kg: ", t)
print("Visina u cm: ", v)
print("Odnos telesna masa/visina iznosi: ", odnos)

if odnos <= 20:
    print("Vasa telesna masa je nedovoljna za vasu visinu!")
elif odnos > 20 and odnos <=25:
    print("Vasa telesna masa odgovara vasoj visini!")
elif odnos > 25 and odnos <= 30:
    print("Vasa telesna masa je prevelika za vasu visinu")
else:
    print("Imate ozbiljan problem sa telesnom tezinom")

# --------------- Python 36 ---------------
# -------------- Zbir kubova --------------

# Faktorizacija zbira kubova vrsi se prema sledecem pravilu:

a = float(input("Unesi vrednost a: "))
b = float(input("Unesi vrednost b: "))

zbirKubova = ((a + b)*(a**2 - a*b + b**2))
print("a ** 3 + b ** 3 ", zbirKubova)
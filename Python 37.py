
# --------------- Python 37 ---------------
# ------------ Razlika kubova -------------

# Faktorizacija razlike kubova vrsi se prema sledecem pravilu:

a = float(input("Unesi vrednost a: "))
b = float(input("Unesi vrednost b: "))

razlikaKubova = ((a - b)*(a**2 + a*b + b**2))
print("a ** 3 - b ** 3 = ", razlikaKubova)
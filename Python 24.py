
# --------------- Python 24 ---------------
# --------- Kontrola toka - while ---------

a = 2

# Osnovna sintaksa petlje
while a < 20:
    print(a)
    a += 2

print('\r')
# Program koji sabira prirodne brojeve (1+2+3+...+n-1+n)

n = int(input("Unesi vrednost n: "))

zbir = 0
x = 1

while x <= n:
    zbir = zbir + x
    x += 1

print("Zbir brojeva od 1 do ", n, "je", zbir)

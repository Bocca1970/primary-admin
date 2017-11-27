
# --------------- Python 9 ---------------
# ------- Najveci uneti broj je: ---------

print("Unesi bilo koja 3 realna broja!!!")
print('\r')
x = float(input('Unesi broj 1: '))
y = float(input('Unesi broj 2: '))
z = float(input('Unesi broj 3: '))

print('\r')

if (x >= y) and (x >= z):
    izaberi = x
elif (y >= x) and (y >= z):
    izaberi = y
else:
    izaberi = z

print("Najveci broj je ----- ",izaberi)


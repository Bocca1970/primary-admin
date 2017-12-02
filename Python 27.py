
# --------------- Python 27 ---------------
# -------- range() funkcija - primer ------


# Funkcija range() koristi paremetre (start), (stop), (step)

a = int(input("Unesi pocetnu vrednost - start: "))
b = int(input("Unesi krajnju vrednost - stop: "))
c = int(input("Unesi vrednost koraka: "))

for n in range(a, b, c):
        if n == 1:
                print('1')    
        elif n == 2:
                print('2')
        else:
                print('{0}'.format(n))
                
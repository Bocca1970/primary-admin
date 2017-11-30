
# --------------- Python 25 ---------------
# -------- Kontrola toka - for Loop -------

parniBrojevi = [2, 4, 6, 8, 10]

# Osnovna sintaksa for petlje
for n in parniBrojevi:
    print(n)

# Provera da li je broj paran ili neparan
broj = int(input("Unesi broj: "))

if broj % 2 == 0:
    if broj % 2 == 0 and broj != 0:
        print("Uneli ste paran broj!")
    elif broj == 0:
        print("Nula nije ni paran ni neparan broj!")
    
else:
    print("Uneli ste neparan broj!")
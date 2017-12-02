
# --------------- Python 26 ---------------
# ---- Kontrola toka - range() funkcija ---


# Funkcija range() koristi paremetre (start), (stop), (step)

# Parametar (stop)
for n in range (12):
    print(n, end="") # Rezultat: 01234567891011

print('\r')

# Parametri (start), (stop)

for m in range (6, 12):
    print(m, end="") # Rezultat: 67891011

print('\r')

# Parametri (start), (stop), (step)

for p in range (4, 12, 2):
    print(p, end="") # Rezultat: 46810
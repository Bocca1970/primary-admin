
# --------------- Python 16 ---------------
# ---- Pregled Matematickih funkcija II ---

import math

# Vraca broj koji se dobije kada se prvi argument stepenuje drugim argumentom
print(math.pow(12, 2)) # Rezultat: 144.0
print(math.pow(12, 3)) # Rezultat: 1728.0
print('\r')

# Vraca kvadratni koren zadatog broja
print (math.sqrt(12)) # Rezultat: 3.4641016151377544
print('\r')

# Vraca vrednost eksponenta zadatog broja
print(math.exp(12)) # Rezultat: 162754.79141900392
print("\r")

# Rastavlja zadati broj na mantisu i eksponent
print(math.frexp(12)) # Rezultat: (0.75, 4)
print('\r')

# Racuna broj na osnovu zadane mantise i eksponenta
print(math.ldexp(12,4)) # Rezultat: 192.0
print('\r')

# Vraca zbir svih clanova niza
zbir = [12, 4.43, 0.021, 11.34] 
print(math.fsum(zbir)) # Rezultat: 27.791
print('\r')





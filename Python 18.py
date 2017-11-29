
# --------------- Python 18 ---------------
# ---------- Pitagorina teorema ------------

import math

x = float(input("Duzina prve katete je: "))
y = float(input("Duzina druge katete je: "))

def hipotenuza(x, y):
    n = x**2
    m = y**2
   
    duzina = math.sqrt(n + m)
    return duzina

print('\r')

print ("Duzina hipotenuze je: ", (hipotenuza(x, y)),)
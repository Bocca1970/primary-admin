
# --------------- Python 30 ---------------
# ------ Resavanje linearne jednacine -----

from sympy import *

x, y, z, a, b, c = symbols('x, y, z, a, b, c')

# Za resavanje linearnih jednacina koristi se funkcija 'linsolve'

# Postavlja se linearni sistem jednacina: 
                                         # 4x + 6y + 8z = 32 
                                         # x + 2y + 3z = 10 
                                         # 3x + 4y + z = 18

a = [4 * x + 6 * y + 8 * z - 32, x + 2 * y + 3 * z - 10, 3 * x + 4 * y + z - 18]

linJednacina = linsolve (a, x, y, z); linJednacina

print(linJednacina)

# Resenje linearnih jednacina je: (3, 2, 1)
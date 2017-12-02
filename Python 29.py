
# --------------- Python 29 ---------------
# ------ Resavanje kvadratne jednacine ----

from sympy import *

x, y, z, a, b, c = symbols('x, y, z, a, b, c')

# Za resavanje kvadratne jednacine koristi se funkcija 'solveset'

# Postavlja se jednostavna jednacina: 2*x**2 = 2

kvadJednacina = solveset (2 * x ** 2 - 2, x); kvadJednacina

print(kvadJednacina)

# Pronadjena su oba resenja (-1,1)


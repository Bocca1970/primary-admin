
# --------------- Python 12 ---------------
# ----------- Koriscenje Modula -----------

import math # Naredba 'import' omogucava pristup specijalizovanim modulima

from math import pi # Naredba 'import' moze omoguciti pristup i podrazumevanom delu radnog prostora
print(pi)

def saPonavljanjem(): # Koriscenje modula u oviru funkcije
    print(math.pi * 2)
    print(math.pi * 3)
    print(math.pi * 4)
    print(math.pi * 5)

saPonavljanjem()

# Kombinovanje modula

math.sin(math.pi/4) 

a = (math.sqrt(5) + 1) / 2
print(a)

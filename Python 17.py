
# --------------- Python 17 ---------------
# ------------- Povrsina kruga ------------

import math

poluprecnik = float(input("Unesi duzinu poluprecnika: "))

def povrsina(poluprecnik):
    p = math.pi * poluprecnik**2
    return p
print('\r')

print ("Povrsina kruga je: ", povrsina(poluprecnik))
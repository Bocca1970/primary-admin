
# --------------- Python 14 ---------------
# ----- Konverzija radijana u stepene -----

import math 

radijan = float(input("Unesi radijan: "))

stepen = round(math.degrees(math.asin(radijan)), 1)
print(stepen)
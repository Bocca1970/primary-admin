
# --------------- Python 13 ---------------
# ----- Konverzija stepena u radijane -----

import math 

stepen = float(input("Unesi stepen: "))

radijan = stepen / 360.0 * 2 * math.pi
print(math.sin(radijan))


# --------------- Python 38 ---------------
# ---------- Pojam Stepenovanja -----------

# Matematicka binarna operacija u zapisu x**n

import math

a = int(input("Unesi vrednost a: "))
b = int(input("Unesi vrednost b: "))


def stepen(a, b):
    if (a<=0 or b<=0):
        return 0
    else:
        print("{0} stepenovano na {1} iznosi {2}".format(a, b, math.pow(a, b)))
        
stepen(a, b)
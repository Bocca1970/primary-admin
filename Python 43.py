
# --------------- Python 43 ---------------
# ---------- Stepenovanje stepena ---------

# (x na n) na m = a na n*m

a = int(input("Unesi vrednost osnove x: "))
b = int(input("Unesi vrednost stepena n: "))
c = int(input("Unesi vrednost stepena m: "))
zbir = (a**(b*c))


def stepen(a, b, c):
    if (a<=0 or b<=0 or c<=0):
        return 0
    else:
        print("{0} na {1} na {2} = {3}".format(a, b, c, zbir))
        
stepen(a, b, c)

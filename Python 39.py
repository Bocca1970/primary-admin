
# --------------- Python 39 ---------------
# ------ Stepenovanje sa istom osnovom ----

# Osnova ostaje ista, eksponenti se sabiraju: x**n * x**m = x**n+m

a = int(input("Unesi vrednost osnove x: "))
b = int(input("Unesi vrednost stepena n: "))
c = int(input("Unesi vrednost stepena m: "))
zbir = (a**(b+c))

def stepen(a, b, c):
    if (a<=0 or b<=0 or c<=0):
        return 0
    else:
        print("{0} na {1} * {0} na {2} = {3}".format(a, b, c, zbir))
        
stepen(a, b, c)
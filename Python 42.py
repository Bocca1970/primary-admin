
# --------------- Python 42 ---------------
# - Deljenje stepena sa istim eksponentom -

# Osnova se menja, eksponent ostaje isti: x**n / y**n = (x/y)**n

a = int(input("Unesi vrednost osnove x: "))
b = int(input("Unesi vrednost osnove y: "))
c = int(input("Unesi vrednost stepena n: "))
razlika = ((a/b)**c)


def stepen(a, b, c):
    if (a<=0 or b<=0 or c<=0):
        return 0
    else:
        print("{0} na {2} / {1} na {2} = {3}".format(a, b, c, razlika))
        
stepen(a, b, c) 
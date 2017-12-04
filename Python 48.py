
# --------------- Python 48 ---------------
# ---- Racunske operacije sa razlomcima ---

# Sabiranje, oduzimanje, mnozenje i deljenje razlomaka 

from fractions import Fraction

a = int(input("Unesi vrednost A: "))
b = int(input("Unesi vrednost B: "))
c = int(input("Unesi vrednost C: "))
d = int(input("Unesi vrednost D: "))


def razlomak(a, b, c, d):
    if (a==0 or b==0 or c==0 or d==0):
        return 0
    else:
        pass

    # A/B + C/D
    zbir = ((a*d+b*c)/(b*d))

    # A/B - C/D
    razlika = ((a*d-b*c)/(b*d))

    # A/B * C/D
    proizvod = ((a*c)/(b*d))

    # A/B / C/D
    kolicnik = ((a*d)/(b*c))

    print(a,'/',b, '+', c,'/',d, '=', Fraction(zbir))
    print(a,'/',b, '-', c,'/',d, '=', Fraction(razlika))
    print(a,'/',b, '*', c,'/',d, '=', Fraction(proizvod))
    print(a,'/',b, '/', c,'/',d, '=', Fraction(zbir))
        
razlomak(a, b, c, d)
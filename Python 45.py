
# --------------- Python 45 ---------------
# -- Mnozenje korena sa istim eksponentom -

# n-ti koren iz x * n-ti koren iz y = n-ti koren iz x*y

a = int(input("Unesi vrednost osnove x: "))
b = int(input("Unesi vrednost osnove y: "))
c = int(input("Unesi vrednost korena n: "))

koren = (a**(1/float(c)) * b**(1/float(c)))

def stepen(a, b, c):
    if (a<=0 or b<=0 or c<=0):
        return 0
    elif c == 2:
        print("Kvadradni koren od {0} * kvadratni koren od {1} = {3}".format(a, b, c, koren))
    elif c == 3:
        print("Kubni koren od {0} * kubni koren od {1} = {3}".format(a, b, c, koren))
    else:
        print("{2}-ti koren od {0} * {2}-ti koren od {1} = {3}".format(a, b, c, koren))

stepen(a, b, c)
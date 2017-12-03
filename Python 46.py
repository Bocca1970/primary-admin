
# --------------- Python 46 ---------------
# ---- Mnozenje korena sa istom osnovom ---

# m-ti koren od n-tog korena od x = n*m koren iz x

a = int(input("Unesi vrednost osnove x: "))
b = int(input("Unesi vrednost korena n: "))
c = int(input("Unesi vrednost korena m: "))

def koren(a, b, c):
    if (a<=0 or b<=0 or c<=0):
        return 0
    else:
        pass

    stepen = (a**(1/float(b*c)))

    if b == 2 or b == 3 and c == 2 or c == 3:
        if b == 2 and c == 2:
            print("Kvadradni koren od kvadratnog korena od {0} = {3}".format(a, b, c, stepen))
        elif b == 2 and c == 3:
            print("Kvadratni koren od kubnog korena od {0} = {3}".format(a, b, c, stepen))
        elif b == 3 and c == 2:
            print("Kubni koren od kvadratnog korena od {0} = {3}".format(a, b, c, stepen))
        elif b == 3 and c == 3:
            print("Kubni koren od kubnog korena od {0} = {3}".format(a, b, c, stepen))        
 
   
    if b != 2 or b != 3 or c != 2 or c != 3:
        if c == 2 and b >= 4:
            print("{1}-i koren od kvadratnog korena od {0} = {3}".format(a, b, c, stepen))
        elif b == 2 and c >= 4:
            print("Kvadratni koren od {2}-og korena od {0} = {3}".format(a, b, c, stepen))
        elif c == 3 and b >= 4:
            print("{1}-i koren od kubnog korena od {0} = {3}".format(a, b, c, stepen))
        elif b == 3 and c >= 4:
            print("Kubni koren od {2}-og korena od {0} = {3}".format(a, b, c, stepen))
        else: 
            print("{1}-i koren od {2}-og korena od {0} = {3}".format(a, b, c, stepen))

koren(a, b, c)
  
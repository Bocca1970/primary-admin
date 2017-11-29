
# --------------- Python 15 ---------------
# ----- Provera deljivosti dva broja ------

broj1 = int(input("Unesi prvi broj: "))
broj2 = int(input("Unesi drugi broj: "))
d = broj1 / broj2
print('\r')

if broj1 % broj2 == 0:
    print("Kada broj {0} podelimo brojem {1} dobijamo ------------- {2}: ".format(broj1,broj2,d))

else:
    print("Broj {0} nije deljiv brojem {1}".format(broj1,broj2))
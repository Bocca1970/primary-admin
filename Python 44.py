
# --------------- Python 44 ---------------
# ----- Izracunavanje kvadratnog korena ---

# Funkcija koren pronalazi delioca argumenta koji stepenovan eksponentom daje argument

osnova = int(input("Unesi vrednost osnove x: "))
kvKoren = 2
stepen = (osnova**(1/float(kvKoren)))

def kvadratniKoren(osnova, kvKoren):
    if osnova <= 0:
        return 0
    elif osnova == 1:
        return 1
    else:
        pass
 

    while True:

        if kvKoren == 2:
            print("Kvadradni koren od {0} = {2}".format(osnova, kvKoren, stepen))
            break
       
  
kvadratniKoren(osnova, kvKoren)
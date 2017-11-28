
# --------------- Python 11 -----------------
# -------- Izracunavanje faktorijela --------

print("---------- Izracunaj faktorijel ----------")
print('\r')
broj = int(input("Unesi broj: "))
print('\r')

def fct(broj):
    blank = ' ' * (2 * broj)
    print(blank, 'faktorijel', broj)
    print('\r')
    if broj == 0:
        print (blank, 'rezultat je: 1')
        print('\r')
        return 1
    else:
        nastavak = fct(broj-1)
        result = broj * nastavak
        print (blank, 'rezultat je: ', result)
        print('\r')
        return result

print ("Faktorijal broja ", broj, "je", fct(broj))

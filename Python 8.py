
# --------------- Python 8 ---------------
# ------- Proveri vrednost izraza --------

print ("Unesi brojeve za izracunavanje vrednosti brojevnog izraza:")
print ("\r")
print ("a * (b + n) / m = :")
print ('\r')

a = input('Unesi vrednost a: ')
print("\r")
print('                        Vas prvi broj je------------------ ',a)
b = input('Unesi vrednost b: ')
print("\r")
print('                        Vas drugi broj je------------------ ',b)
n = input('Unesi vrednost n: ')
print("\r")
print('                        Vas treci broj je------------------ ',n)
m = input('Unesi vrednost m: ')
print("\r")
print('                        Vas cetvrti broj je------------------ ',m)

c = float(a) * (float(b) + float(n)) / float(m)

print('\r')
print ('     Dobili ste {0} * ({1} + {2}) / {3} = {4}'.format(a,b,n,m,c))
print('\r')



# --------------- Python 16 ---------------
# --------- Dok traje odbrojavanje --------

import time

b = int(input('Unesi broj: '))

def odbrojavanje(b):
    if b <= 0:
        print('NULA!!!')
       
    else:
        print (b)
        time.sleep(1)
        odbrojavanje (b-1)
        time.sleep(0.1)
            
odbrojavanje(b)

print('\r')

def dodatak(izraz, ponavljanje):
    if ponavljanje <= 0:
        return
    print (izraz)
    time.sleep(1)
    dodatak(izraz, ponavljanje-1)

dodatak("Dok traje odbrojavanje....", 3)
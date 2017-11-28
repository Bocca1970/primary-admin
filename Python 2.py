
# --------------- Python 2 ----------------
# ------- Tipovi podataka - Nizovi --------

s = '12asd34KL'
print(type(s)) # string - konacni uredjeni skup koji se nalazi izmedju navodnika
# class 'str'

l = [10, 'lista', 23.34]
print(type(l)) # list - konacni uredjeni skup koji se nalazi unutar uglastih zagrada
# class 'list' 

t = (12, 'asd', '34KL')
print(type(t)) # tuple - konacni uredjeni skup, kao i 'list', samo sto je ovaj skup nepromenljiv 
# class 'tuple'

c = {10, 1, 20, 2, 30, 3, 40, 4, 50, 5}
print(type(c)) # set - neuredjeni skup jedinstvenih karaktera unutar viticastih zagrada
# class 'set' 

d = {'Ime:' : 'Bocca', 'Key' : 'Value'}
print(type(d)) # dict - recnik vrsi mapiranje kljuca (key) u neku odredjenu vrednost (value)
# class 'dict'
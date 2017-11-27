
# --------------- Python 4 ---------------
# --------- Konverzija - Nizovi ----------

l = set([2, 4, 6])
print(type(l)) # Konverzija uredjenog skupa 'list' u neuredjeni skup 'set'
# class 'set'

s = list({3, 5, 7})
print(type(s)) # Konverzija neuredjenog skupa 'set' u uredjeni skup 'list'
# class 'list'

m = list('hello')
print(type(m)) # Konverzija izmedju dva uredjena skupa 'string' u 'list'
# class 'list'

n = str([10, 20, 30])
print(type(n)) # Konverzija izmedju dva uredjena skupa 'list' u 'string'
# class 'str'

t = set([5, 'dva', 3])
print(type(t)) # Konverzija nepromenljivog skupa 'tuple' u jedinstveni skup 'set'
# class 'set'

i = dict([[1, 11], [2, 22]])
print(type(i)) # Kod konverzije u recnik, samo napraviti parove 'key:value'
# class 'dict'




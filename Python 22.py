
# --------------- Python 22 ---------------
# -------- Kontrola toka - if...else ------

a = 3
b = 2

# Osnovna sintaksa kontrole toka izvrsenja
if a > b:
    print("a je vece od b")
elif a == b:
    print("a je jednako b")
else:
    print("a je manje od b")

x = 0
y = 101
z = 100

# Kontrola toka korisenjem standardnih logickih operatora
if y > x and y < z:
    print("y je unutar opsega")
elif y < x or y > z:
    print("y je izvan opsega")
else:
    print("y je jednako granicnim vrednostima")


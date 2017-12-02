
# --------------- Python 31 ---------------
# ---------- Distributivni zakon ----------

# (a+b)*(c+d) = ac + ad + bc + bd

a = float(input("Unesi vrednost a: "))
b = float(input("Unesi vrednost b: "))
c = float(input("Unesi vrednost c: "))
d = float(input("Unesi vrednost d: "))

disZakon = (a*c + a*d + b*c + b*d)
print("(a + b) * (c + d) = ", disZakon)
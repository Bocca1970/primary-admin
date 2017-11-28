
# --------------- Python 10 ---------------
# ----------- Logicke Operacije -----------

import operator
 
x = True
y = False

# Binarni operator logicko i (&):
print ("binarni operator logicko i - x&y je: ", end="")
print (operator.and_(x, y))

# Binarni operator logicko ili (|):
print ("binarni operator logicko ili - x|y je: ", end="")
print (operator.or_(x, y))

# Unarni operator negacije (~x):
print ("Unarni operator negacije - ~x: ", end="")
print (operator.not_(x))

''' Operand 1     and      or    Operand 2
     True        True     True    True
     True        False    True    False
     False       False    True    True
     False       False    False   False
'''



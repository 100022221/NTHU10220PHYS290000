H = raw_input("�п�J�𪺰���")
H = float(H)

h = raw_input("�п�J�ҨD����")
h = float(h)

import math

if h <= H:
    t = math.sqrt((H-h)/(0.5*9.8))
    T = math.sqrt(H/(0.5*9.8))
    print T-t
    

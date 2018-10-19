"""
Решение квадратного уравнения с целыми корнями
"""
import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
D = b*b-4*a*c
print(f'D={D}')
if D > 0:
    x1 = (b - math.sqrt(D))/2/a
    x2 = (b + math.sqrt(D))/2/a
    print(f'x1 = {x1}, x2 = {x2}')
elif D == 0:
    print(f'x = {b-math.sqrt(D)}')
else:
    print("d < 0 and has'n solution!!!")

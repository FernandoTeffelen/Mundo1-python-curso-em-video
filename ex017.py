from math import hypot
from math import radians, sin, cos, tan
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
print('A hipotenusa vai medir {:.2f}'.format(hi))
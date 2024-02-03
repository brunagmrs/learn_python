#Equação do segundo grau
from math import sqrt
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = b ** 2 - 4 * a * c
raiz = sqrt(delta)
x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)
print(f'OS valores de x para essa equação é {x1} e {x2}')

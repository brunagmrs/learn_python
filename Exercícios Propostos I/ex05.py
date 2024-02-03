#Distância entre dois pontos
from math import sqrt
x1 = float(input('Digite a cordenada de P1: '))
y1 = float(input())
x2 = float(input('Digite a cordenada de P2: '))
y2 = float(input())
num = sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'A distância entre os pontos P1 e P2 é de {num}')

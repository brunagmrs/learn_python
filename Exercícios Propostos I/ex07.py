#Salário Corretor
nome = str(input('Digite seu nome: '))
qtdv = int(input('Digite a quantidade de imóveis vendidos: '))
val = float(input('Digite o valor de total de vendas '))
qtdv = float(qtdv)
sal = float(1500 + (200*qtdv) + (0.5 * val))
print(f'O valor do Sálario de {nome} é {sal}')

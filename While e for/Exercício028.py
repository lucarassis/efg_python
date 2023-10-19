'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

quantCD = int(input("Digite a quantidade de CDs: "))
aux = 0
total = 0

for x in range(quantCD):
	valorCD = float(input(f'Digite o valor do CD {x+1} de {quantCD}: '))
	total = total + valorCD
	valorMedio = total / quantCD
	aux += 1

print(f"*"*60)
print(f'O valor total gasto: R$ {total:2.2f}')
print(f'O valor médio gasto por cada CD foi de: R$ {valorMedio:2.2f}')
print(f'*'*60)
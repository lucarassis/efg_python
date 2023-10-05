'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque 
e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, 
o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, 
o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

numero = int(input('Valor para sacar entre [10-600]: '))

cem = int(numero / 100)
numero = numero - (cem*100)
    
cinquenta = int(numero/50)
numero = numero - (cinquenta*50)

dez = int(numero/10)
numero = numero - (dez*10)

cinco = int(numero/5)
numero = numero - (cinco*5)

um = numero
    
print(f'Notas R$ 100,00 = {cem:2.0f}')
print(f'Notas R$  50,00 = {cinquenta:2.0f}')
print(f'Notas R$  10,00 = {dez:2.0f}')
print(f'Notas R$   5,00 = {cinco:2.0f}')
print(f'Notas R$   1,00 = {um:2.0f}')




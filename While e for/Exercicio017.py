'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120'''

fatorial = int(input('Digite o número do fatorial a ser pesquisado: '))
contador = fatorial
fat = 1
print(f'Calculando {fatorial}! = ', end="")
while contador > 0:
    print(f'{contador} ', end="")
    print(' x ' if contador > 1 else ' = ', end='')
    fat *= contador
    contador -= 1
print(f'{fat}')


'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão).'''

numero = int(input('Digite um número entre [1 - 5350]: '))

if numero > 0 and numero <= 5350:
    if numero % 2 == 0:
        print('O número digitado', numero, 'é par')
    else:
        print('O numero digitado', numero, 'é impar')
else:
    print("Número digitado é inválido. Digite entre [1 e 5350]")
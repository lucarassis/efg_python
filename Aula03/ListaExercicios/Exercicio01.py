# Faça um programa que peça dois números e imprima o maior deles.

numero1 = input('Digite o primeiro número: ')

numero2 = input('Digite o segundo número: ')

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    if numero1 > numero1:
        print('O número', numero1, 'é maior que o número', numero2)
    elif numero1 == numero2:
        print('Os números são iguais')
    else:
        print('O número', numero2, 'é menor que o número', numero1)
except Exception:
    exit()
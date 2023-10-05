#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

numero1 = int(input('Digite um valor:'))
numero2 = int(input('Digite outro valor, diferente do primeiro: '))

try:
    resultado = numero1 - numero2
    if resultado < 0:
        print('O resultado é negativo', resultado)
    else:
        print('O resultado é positivo', resultado)
except Exception:
    exit()

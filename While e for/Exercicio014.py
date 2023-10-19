'''Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a quantidade de números impares.
lista = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero %2 == 0:
        print(f'O número é {numero} par.')
    else:
        print(f'O número {numero} é impar')'''

pares = 0
impares = 0
for _ in range(10):
    if int(input("Digite um numero: ")) % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Você digitou {pares} números pares: \nVocê digitou {impares} números ímpares:")

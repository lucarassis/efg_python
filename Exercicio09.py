#Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for n in range(3): # o valor entre parenteses representa a quantida de números que desejo. No caso do exemplo. 3
    n = int(input(f'Digite os valores em N{n+1}: '))
    lista.append(n)
print()
lista.sort(reverse=True)
print(lista)
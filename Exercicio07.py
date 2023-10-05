#Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input('Digite primeiro número: ')) # A
numero2 = int(input("Digite o segundo número: ")) # B
numero3 = int(input("Digite o terceiro número: ")) # C
 
maior = numero1

if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3> numero1 and numero3> numero2:
    maior = numero3

print(f'O maior número digitado foi {maior}')

menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
print(f'O menor número digitado foi: {menor}')
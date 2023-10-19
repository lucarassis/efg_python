'''Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.'''

print('Usando while')
num = 0
while num < 20:    
    num += 1
    print(f'Numéro {num}')
print(list(range(1,21)))

print()
print('Usando laço for')

for i in range (1,21):
	print (i)
print(list(range(1,21)))
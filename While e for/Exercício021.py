'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

núm = int(input('Digite um número POSITIVO: '))
divXvezes = 0
for c in range(1, núm+1):
    if núm % c == 0:
        divXvezes += 1
    else:
        print(f'{c}', end='-')
print(f'\nO número {núm} foi divisível {divXvezes} vezes')
if divXvezes == 2:
    print('E por isso ele é um número PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')

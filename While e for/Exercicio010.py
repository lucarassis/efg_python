'''Faça um programa que receba dois números inteiros e gere os números inteiros que 
estão no intervalo compreendido por eles.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print()
for i in range(num1+1, num2):
    print(i)
print('Fim do programa')
print()
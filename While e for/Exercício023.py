'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

def primo(numero):
    div = 0
    for n in range(1, numero+1):
        if numero % n == 0:
            div += 1 
    return div

numero = int(input('Digite um número: '))
lista = [x for x in range(1, numero +1)]
primos = []

for n in lista:
    div = primo(n)
    if div == 2:
        primos.append(n)

print(primos)
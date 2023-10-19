'''Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0] #strip... remover espaços.
print()
print(f'Você digitou {quant} números e a soma dos números é: {soma}')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}')
print()
print(f'Apesar de não ter sido solicitado, mas vou aproveitar e fazer a média: {soma / quant:5.2f}')
print()
'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, 
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite a idade da pessoa pesquisada: '))
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
print(f'Você pesquisou {quant} pessoas e a soma da idade delas é de: {soma} anos')
print()
print(f'O mais velho tem {maior} anos e o mais novo tem {menor} anos')
print()
print(f'A idade média é: {soma/quant:2.0f} anos, portanto, ', end='')

média = soma / quant
if média < 26:
    print('jovem.')
elif média < 61:
    print('adulta.')
else:
    print('idosa.')
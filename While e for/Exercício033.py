'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia 
as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite a temperatura da sua cidade: '))
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

print('*'*90)
print(f'Você pesquisou {quant} cidades e a soma das temperaturas delas foi: {soma} graus')
print()
print(f'A MAIOR temperatura foi {maior} graus e a MENOR temperatura {menor} graus')
print()
print(f'A temperatura média é de: {soma/quant:2.0f} graus.', end='')

média = soma / quant
if média < 23:
    print(' Temperatura FRESCA.')
elif média < 30:
    print(' Temperatura AMENA.')
else:
    print(' Temperatura ALTA, ingerir bastante água.')
print('*'*90)

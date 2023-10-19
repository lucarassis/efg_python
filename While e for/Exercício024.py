#Faça um programa que calcule o mostre a média aritmética de N notas.

resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    núm = float(input('Digite uma nota: '))
    soma += núm
    quant += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0] #strip... remover espaços.
print()
print(f'Você digitou {quant} notas. Média do aluno foi: {soma / quant:5.2f}')
print()
 
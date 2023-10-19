'''Faça um programa que leia 5 números e informe o maior número.'''

maior = 0 
for m in range(1,6): # m - pode ser qualquer letra, não importa no resultado.
    número = int(input(f'Digite o {m}º número: '))
    if m == 1:
        maior = número
    else:
        if número > maior:
            maior = número
    
print(f'O Maior número foi: {maior}')

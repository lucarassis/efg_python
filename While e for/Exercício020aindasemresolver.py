'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
fatorial várias vezes e limitando o fatorial a 
números inteiros positivos e menores que 16.'''

fatorial = int(input('Digite o número do fatorial a ser pesquisado: '))
contador = fatorial
fat = 1
resp = 'S'
print(f'Calculando {fatorial}! = ', end="")
while resp in 'Ss':
    if contador > 0 and contador <= 16:
        print(f'{contador} ', end="")
        print(' x ' if contador > 1 else ' = ', end='')
        fat *= contador
        contador -= 1
    else:   
        print(f'{fat}')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
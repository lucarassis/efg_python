#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# Professor Guanabara

ano = int(input('Digite o ano a ser pesquisado: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO é bissexto')

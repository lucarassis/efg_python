'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de 
centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 
25, 20, 10, 21, 11, 1, 7 e 16'''

numero = int(input('Digite um número entre 1 e 1000: '))

if numero == 1:
    print('0 Centenas, 0 Dezenas e 1 unidade')
elif numero > 1 and numero <= 100:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    print(f'0 Centenas, {dezena:2.0f} Dezenas e {unidade} unidades')
elif numero > 100 and numero <= 1000:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100)
    print(f'{centena:2.0f} Centenas, {dezena:2.0f} Dezenas e {unidade} unidades')
else:
    print('Número inválido, digite de 1 a 1000')
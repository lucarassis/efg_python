'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

operacaodesejada = input('Qual operação desejada (+, -, /, //, *,**):')

if operacaodesejada == '+':
    resultado = numero1 + numero2
    if resultado % 2 == 0:
        print(f'O número {resultado} é par')
    else:
        print(f'O número {resultado} é impar')
    if resultado >=0:
        print(f'O número {resultado} é positivo')
    else:
        print(f'O número {resultado} é negativo')
    if round(resultado) == resultado:
        print(f'O número {resultado} é inteiro')
    else:
        print(f'O número {resultado} é decimal')
    
if operacaodesejada == '-':
    resultado = numero1 - numero2
    if resultado % 2 == 0:
        print(f'O número {resultado} é par')
    else:
        print(f'O número {resultado} é impar')
    if resultado >=0:
        print(f'O número {resultado} é positivo')
    else:
        print(f'O número {resultado} é negativo')
    if round(resultado) == resultado:
        print(f'O número {resultado} é inteiro')
    else:
        print(f'O número {resultado} é decimal')
    
if operacaodesejada == '/':
    resultado = numero1 / numero2
    if resultado % 2 == 0:
        print(f'O número {resultado} é par')
    else:
        print(f'O número {resultado} é impar')
    if resultado >=0:
        print(f'O número {resultado} é positivo')
    else:
        print(f'O número {resultado} é negativo')
    if round(resultado) == resultado:
        print(f'O número {resultado} é inteiro')
    else:
        print(f'O número {resultado} é decimal')

if operacaodesejada == '//':
    resultado = numero1 // numero2
    if resultado % 2 == 0:
        print(f'O número {resultado} é par')
    else:
        print(f'O número {resultado} é impar')
    if resultado >=0:
        print(f'O número {resultado} é positivo')
    else:
        print(f'O número {resultado} é negativo')
    if round(resultado) == resultado:
        print(f'O número {resultado} é inteiro')
    else:
        print(f'O número {resultado} é decimal')

if operacaodesejada == '*':
    resultado = numero1 * numero2
    if resultado % 2 == 0:
        print(f'O número {resultado} é par')
    else:
        print(f'O número {resultado} é impar')
    if resultado >=0:
        print(f'O número {resultado} é positivo')
    else:
        print(f'O número {resultado} é negativo')
    if round(resultado) == resultado:
        print(f'O número {resultado} é inteiro')
    else:
        print(f'O número {resultado} é decimal')

if operacaodesejada == '**':
    resultado = numero1 ** numero2
    if resultado % 2 == 0:
        print(f'O número {resultado} é par')
    else:
        print(f'O número {resultado} é impar')
    if resultado >=0:
        print(f'O número {resultado} é positivo')
    else:
        print(f'O número {resultado} é negativo')
    if round(resultado) == resultado:
        print(f'O número {resultado} é inteiro')
    else:
        print(f'O número {resultado} é decimal')
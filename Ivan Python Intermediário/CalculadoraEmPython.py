# '''Crie uma calculadora simples em Python que pode realizar as quatro operações básicas: Adição, subtração, multiplicação e divisão.
# O programa deve pedir ao usuário que escolha uma operação e, em seguida, solicitar dois números. Depois, deve exibir o resultado da operação
# escolhida.
# 1. O programa deve ser capaz de realizar adição, subtração, multiplicação e divisão.
# 2. Deve tratar erros, como divisão por zero.
# 3.O programa deve ser executado em loop para que o usário possa continuar fazendo cálculos até que escolha sair.'''

print('Qual operação deseja: 1. Adição 2. Subtração 3.Multiplicação 4.Divisão ou 5.Sair: ')
print('-'*85)

def adicao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    soma = (num1 + num2)
    print(soma)

def subtracao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    subtracao = (num1 - num2)
    print(subtracao)

def multiplicacao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    multiplicacao = (num1 * num2)
    print(multiplicacao)

def divisao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if num2 == 0:
        print('Valor divisil por zero. Tente outro número: ')
    else:
        print(num1 / num2)

#-----------------------------------------------------------------------

def menu():
    opcao = 1  
    while opcao != 5:
        print('Escolha uma opção abaixo:')
        print('1 - Adição ou soma: ')
        print('2 - Subtracao: ')
        print('3 - Multiplicação: ')
        print('4 - Divisão: ')
        print('5 - Sair: ')

        opcao = int(input('Digite uma das opções ou 5 para sair: '))
        if opcao == 1:
            print('---Iniciando a função Adição ou Soma---')
            adicao()
            print('---Fim da função Adição ou soma---')
        if opcao == 2:
            print('---Iniciando a função Subtração---')
            subtracao()
            print('---Fim da função Subtração---')
        if opcao == 3:
            print('---Iniciando a função Multiplicação---') 
            multiplicacao()
            print('---Fim da função Multiplicação---') 
        if opcao == 4:
            print('---Iniciando a função Divisão---') 
            divisao()
            print('---Fim da função Divisão---') 
            divisao()
#----------------------------------------------------------
# Até aqui o Alencar ensinou.
        else:
            print('Escolha uma das opções disponíveis')

    print('----Fim do menu ----')
        
# Chamar função de menu
menu()
def imprimir_maior_numero():
    numero1 = input("Digite o primeiro número: ")

    numero2 = input("Digite o segundo número: ")

    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        if numero1 > numero2:
            print("O número", numero1, "é maior que o número", numero2)
        elif numero1 == numero2:
            print("Os números são iguais")
        else:
            print("O número", numero2, "é maior que o número", numero1)
    except Exception:
        print("Você não digitou um número válido")
        exit()


def verificar_valor_positivo():
    # Faça um Programa que peça um valor e mostre na tela se o valor é positivo 
    # ou negativo.

    valor = int(input("Digite um valor: "))

    if valor > 0:
        print("O valor é positivo")
    elif valor == 0:
        print("O valor é neutro")
    else:
        print("O valor é negativo")

# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.
# Até aqui o Alencar ensinou

def fem_mas():
    sexo = input('Digite F ou M: ')

    if sexo == "F" or sexo == "f":
        print('F - Feminino')
    elif sexo == 'M' or sexo == "m":
        print('M - Masculino')
    else:
        print('Sexo inválido')

# ---------------------------------------------------------------------------------------
#Faça um programa que verifique se uma letra digitada é vogal ou consoante
def vogal ():
    vogal = input("Digite uma letra do alfabeto, forma minuscula: ")

    if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
        print('A letra digitada é uma vogal')
    elif vogal != ('a', 'e', 'i', 'o', 'u'):
        print('A letra digitada é uma consoante')
    else:
        print("Esta letra não foi digitada na forma solicitada")
# --------------------------------------------------------------------

#Faça um programa para leitura para a leitura de duas notas parciais de um aluno. o Programa deve calcular a média
#alcançada por aluno e apresentar:
# Aprovado maior ou igual a 7
# Reprovado menor que 7
# Aprovado com distinção media igual a 10

def nota_aluno():
    nota1 = float(input('Digite a primeira nota do aluno 0 a 10: '))
    nota2 = float(input('Digite a segunda nota do aluno 0 a 10: '))
    media = ((nota1 + nota2)/2)

    if media == 10:
        print('O aluno está aprovado com distinção, média', media, 'e merece todo nosso respeito e admiração')
    elif media >= 7:
        print("O aluno foi aprovado com média", media)
    else:
        print("O aluno foi reprovado com média", media)
#----------------------------------------------------------------------------------------------

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.
def preco():
    preco1 = float(input("Digite o preço do produto 1: "))
    preco2 = float(input("Digite o preço do produto 2: "))
    preco3 = float(input("Digite o preço do produto 3: "))
    if preco1 < preco2 and preco1 < preco3:
        print(f"O produto com o menor preco é o 1, custando R$ {preco1:2.2f}")
    elif preco2 < preco1 and preco2 < preco3:
        print(f"O produto com o menor preco é o 2, custando R$ {preco2:2.2f}")
    else:
        print(f"O produto com o menor preco é o 3, custando R$ {preco3:2.2f}")
#-----------------------------------------------------------------------------------

#Faça um Programa que leia três números e mostre-os em ordem decrescente.
def quant_num():
    lista = []

    for n in range(3): # o valor entre parenteses representa a quantida de números que desejo. No caso do exemplo. 3
        n = int(input(f'Digite os valores em N{n+1}: '))
        lista.append(n)
    print()
    lista.sort(reverse=True)
    print(lista)
#----------------------------------------------------------------------------------------------------------
# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def turno_M_V_N():
    turno = input("Digite seu turno, M - matutino, V - vespertino, N - noturno: ").upper()
    if turno == "M":
        print("Bom dia!")
    elif turno == "V":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Valor inválido!")
#-----------------------------------------------------------------------
'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

def aumento_salario():
    salarioAnterior = float(input('Digite seu salário R$: '))
    salarioAposAumento = 0
    diferencaSalarial = 0
    percentualDeAumento = 0

    if salarioAnterior <= 280:
        percentualDeAumento = 20
    elif salarioAnterior <= 700:
        percentualDeAumento = 15
    elif salarioAnterior <= 1500:
        percentualDeAumento = 10
    else:
        percentualDeAumento = 5

    diferencaSalarial = salarioAnterior * (percentualDeAumento / 100)
    salarioAposAumento = salarioAnterior + diferencaSalarial

    print(f'Seu salário antes do reajuste era de R$ {salarioAnterior:5.2F}')
    print(f'Seu salário foi aumentado em {percentualDeAumento}%')
    print(f'O valor do aumento em seu salário foi de R$ {diferencaSalarial:5.2f}')
    print(f'Seu novo salário, após o aumento é de R$ {salarioAposAumento:5.2f}')






def menu():
    opcao = 1  
    while opcao != 0:
        print('----Seja bem vindo ao meu Super Menu----')
        print('Escolha uma opção abaixo:')
        print('1 - Imprimir maior número: ')
        print('2 - Verificar se o valor é positivo ou negativo: ')
        print('3 - Verificar Fem ou Masc: ')
        print('4 - Verificar vogal: ')
        print('5 - Veja nota do aluno: ')
        print('6 - Preço dos produtos: ')
        print('7 - Escolha quantos números quer digitar: ')  
        print('8 - Digite seu turno M V N: ')  
        print('9 - Aumento salário: ')
        opcao = int(input('Digite uma das opções ou 0 para sair: '))
        if opcao == 1:
            print('---Iniciando a função imprimir_maior_numero---')
            imprimir_maior_numero()
            print('---Fim da função imprimir_maior_numero---')
        if opcao == 2:
            print('---Iniciando a função verificar_valor_positivo---')
            verificar_valor_positivo()
            print('---Fim da função verificar_valor_positivo---')
        if opcao == 3:
            print('Verificar se é Fem ou Mas ') 
            fem_mas() 
        if opcao == 4:
            print('Verificar a vogal ')
            vogal()
        if opcao == 5:
            print('Verificar a nota do aluno: ')
            nota_aluno()
        if opcao == 6:
            print('Verificar o preço dos produtos: ')
            preco()
        if opcao == 7:
            print('Digite 3 números aleatótrios: ')
            quant_num()
        if opcao == 8:
            print('Digite qual seu turno M - V - N: ')
            turno_M_V_N()
        if opcao == 9:
            print('Qual valor atual de seu salário: ')
            aumento_salario()
#----------------------------------------------------------



# Até aqui o Alencar ensinou.
        else:
            print('Opção inválida')

        print('\n----Fim do menu ----')
        
# Chamar função de menu
menu()
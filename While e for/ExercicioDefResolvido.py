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
#-----------------------------------------------------------------------------------------
'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''
def calc_folha_pgto():
    ValorHora = float(input('Digite o valor da hora trabalhada R$: '))
    QdeHoraTrabalhada = float(input('Digite a quantidade horas trabalhadas no mês: '))
    SalarioBruto = ValorHora * QdeHoraTrabalhada

    if SalarioBruto <= 900:
        DescIR = 0
    elif SalarioBruto <=1.500:
        DescIR = 5
    elif SalarioBruto <= 2.500:
        DescIR = 10
    else:
        DescIR = 20
    IR = SalarioBruto * (DescIR / 100)
    INSS = SalarioBruto * (10 / 100)
    Sindicato = SalarioBruto * (3 / 100)
    FGTS = SalarioBruto * (11 / 100)
    DescontosFolha = IR + INSS + Sindicato
    SalarioLiquido = SalarioBruto - DescontosFolha

    print(
        f'\n Salário Bruto : R$ {SalarioBruto:5.2F}',
        F'\n ( - ) IR {DescIR} : R$ {IR:5.2f}',
        f'\n ( - ) INSS (10%): R$ {INSS:5.2f}'
        f'\n ( - ) Sindicato: R$ {Sindicato:5.2f}'
        f'\n FGTS (11%) : R$ {FGTS:5.2f}'
        f'\n Descontos Folha : R$ {DescontosFolha:5.2f}'
        f'\n Salário Líquido : R$ {SalarioLiquido:5.2f}'
    )
#-------------------------------------------------------------------------------------
'''Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

def dia_da_semana():
    DiaSemana = int(input('1-Domingo, 2-Segunda, 3-Terça, 4-Quarta, 5-Quinta, 6-Sexta, 7-Sábado :'))

    if DiaSemana == 1:
        print('1-Domingo')
    elif DiaSemana == 2:
        print('2-Segunda')
    elif DiaSemana == 3:
        print('3-Terça')
    elif DiaSemana == 4:
        print('4-Quarta')
    elif DiaSemana == 5:
        print('5-Quinta')
    elif DiaSemana == 6:
        print('6-Sexta')
    elif DiaSemana == 7:
        print('7-Sábado')
    else:
        print('Valor inválido. Digite de 1 a 7 ')
#---------------------------------------------------------------------------
'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''
def nota_do_aluno():
    lista = []
    for n in range (2):
        n = int(input(f'Digite a nota do aluno Nota{n+1}: '))
        lista.append(n)    
    media = (sum(lista)/2)

    if media >= 9:
        print(f'Média {media:5.2f} Conceito A - Aprovado')
    elif media >= 7.5:
        print(f'Média {media:5.2f} Conceito B - Aprovado')
    elif media >= 6:
        print(f'Média {media:5.2f} Conceito C - Aprovado')
    elif media >= 4:
        print(f'Média {media:5.2f} Conceito D - REprovado')
    else:
        print(f'Média {media:5.2f} Conceito E - REAprovado')
#---------------------------------------------------------------------------------
'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
def lado_triangulo():
    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))

    if (
        (lado1 + lado2 > lado3)
        and (lado1 + lado3 > lado2)
        and (lado2 + lado3 > lado1)
    ):
        if (lado1 == lado2) and (lado2 == lado3):
            print("É um triângulo equilátero!")
        elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
            print("É um triângulo isósceles!")
        else:
            print("É um triângulo escaleno!")
    else:
        print("Não é um triângulo!")

    # este não entendi muito bem.
#-----------------------------------------------------------------------

'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
def raizes_equacao():
    a = float(input("Digite o valor de a: "))
    if a == 0:
        print("Não é uma equação do segundo grau")
    else:
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        delta = (b ** 2) - (4 * a * c)
        if delta < 0:
            print("Delta menor que 0. Não há raízes reais.")
        elif delta == 0:
            raiz = (-b) / (2 * a)
            print(f"Delta é zero. A raíz é {raiz:5.2f}")
        else:
            raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
            raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)
            print(
                f"Delta maior que zero. A raíz 1 é {raiz1:5.4f}, e a raiz 2 é {raiz2:5.4f}"
            )
#-----------------------------------------------------------------------------
#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# Professor Guanabara
def ano_bissexto():
    ano = int(input('Digite o ano a ser pesquisado: '))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} NÃO é bissexto')
#---------------------------------------------------------------------
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def data_valida():
    data = input('Digite uma data no formato dd/mm/aaaa: ')

    dia, mes, ano = data.split('/')

    dia, mes, ano = int(dia), int(mes), int(ano)

    valida = False
        
        # Meses com 31 dias
    if( mes==1 or mes==3 or mes==5 or mes==7 or \
            mes==8 or mes==10 or mes==12):
            if(dia<=31):
                valida = True
        # Meses com 30 dias
    elif( mes==4 or mes==6 or mes==9 or mes==11):
            if(dia<=30):
                valida = True
    elif mes==2:
            # Testa se é bissexto
            if (ano%4==0 and ano%100!=0) or (ano%400==0):
                if(dia<=29):
                    valida = True
            elif(dia<=28):
                    valida = True

    if(valida):
            print('Data válida')
    else:
            print('Inválida')

    print(f'{dia}/{mes}/{ano}')
#------------------------------------------------------------------------------
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de 
centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 
25, 20, 10, 21, 11, 1, 7 e 16'''
def inteiro_menor_1000():
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
#----------------------------------------------------------------------------------------
'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve 
calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''
def notas_3_alunos():
    nota1 = float(input('Digite a primeira nota do aluno 0 a 10: '))
    nota2 = float(input('Digite a segunda nota do aluno 0 a 10: '))
    nota3 = float(input('Digite a terceira nota do aluno 0 a 10: '))
    media = ((nota1 + nota2 + nota3)/3)

    if media == 10:
        print(f'O aluno está aprovado com distinção, média {media:.2f} e merece todo nosso respeito e admiração')
    elif media >= 7:
        print(f'O aluno foi aprovado com média: {media:.2f}')
    else:
        print(f'O aluno foi reprovado com média: {media:.2f}')
#-----------------------------------------------------------------------

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
        print('10 - Cálculo folha de pagaento: ')
        print('11 - Dia da semana: ')
        print('12 - Digite a nota do aluno: ')
        print('13 - Digite os lados do triângulo: ')
        print('14 - Digite as raízes de uma equação: ')
        print('15 - Digite ano bissexto: ')
        print('16 - Digite uma data a ser pesquisada: ')
        print('17 - Digite um número inteiro menor que 1000: ')
        print('18 - Digite 3 notas do aluno: ')

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
        if opcao == 10:
            print('Qual cálculo da sua folha de pagamento: ')
            calc_folha_pgto()
        if opcao == 11:
            print('Digite o dia da semana: ')
            dia_da_semana()
        if opcao == 12:
            print('Digite a nota do aluno: ')
            nota_aluno()
        if opcao == 13:
            print('Digite os lados do triângulo: ')
            lado_triangulo()
        if opcao == 14:
            print('Digite as raizes de uma equação: ')
            raizes_equacao()
        if opcao == 15:
            print('Digite Ano bissexto: ')
            ano_bissexto()
        if opcao == 16:
            print('Digite uma data a ser pesquisada: ')
            data_valida()
        if opcao == 17:
            print('Digite um número inteiro menor que 1000: ')
            inteiro_menor_1000()
        if opcao == 18:
            print('Digite 3 notas do aluno: ')
            notas_3_alunos()
#----------------------------------------------------------


# Até aqui o Alencar ensinou.
        else:
            print('Opção inválida')

        print('\n----Fim do menu ----')
        
# Chamar função de menu
menu()
'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''

telefonou = str(input('Você telefonou para a vítima?: (S-Sim N-Não) '))
local = str(input('Você esteve no local do crime?: (S-Sim N-Não) '))
moraPerto = str(input('Você mora perto da vítima?: (S-Sim N-Não) '))
devia = str(input('Você devia para a vítima?: (S-Sim N-Não) '))
jaTrabalhou = str(input('Você já trabalhou com a vítima?: (S-Sim N-Não) '))

if telefonou == "S" or telefonou == "s":
    telefonou = 1
else:
    telefonou = 0

if local == "S" or local == "s":
    local = 1
else:
    local = 0

if moraPerto == "S" or moraPerto == "s":
    moraPerto = 1
else:
    moraPerto = 0

if devia == "S" or devia == "s":
    devia = 1
else:
    devia = 0

if jaTrabalhou == "S" or jaTrabalhou == "s":
    jaTrabalhou = 1
else:
    jaTrabalhou = 0

participacaoCrime = (telefonou + local + moraPerto + devia + jaTrabalhou)

if participacaoCrime == 2:
    print('Suspeita')
elif participacaoCrime == 3 or participacaoCrime == 4:
    print('Cúmplice')
elif participacaoCrime == 5:
    print('Assassino')
else:
    print('Inocente')

print(participacaoCrime)



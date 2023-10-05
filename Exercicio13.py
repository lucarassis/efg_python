'''Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

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
    print('Valor inválido. Digite de 1 a 7')

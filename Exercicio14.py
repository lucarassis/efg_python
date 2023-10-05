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


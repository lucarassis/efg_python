#Faça um programa para leitura para a leitura de duas notas parciais de um aluno. o Programa deve calcular a média
#alcançada por aluno e apresentar:
# Aprovado maior ou igual a 7
# Reprovado menor que 7
# Aprovado com distinção media igual a 10

nota1 = float(input('Digite a primeira nota do aluno 0 a 10: '))
nota2 = float(input('Digite a segunda nota do aluno 0 a 10: '))
media = ((nota1 + nota2)/2)

if media == 10:
    print('O aluno está aprovado com distinção, média', media, 'e merece todo nosso respeito e admiração')
elif media >= 7:
    print("O aluno foi aprovado com média", media)
else:
    print("O aluno foi reprovado com média", media)
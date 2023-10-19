'''Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.'''

turmas = int(input("Digite quantas turmas tem na escola: "))
media = soma = 0
for i in range(turmas):
    while True:
        alunos = int(input(f"Digite quantos alunos tem na turma {i + 1}: "))
        if alunos <= 40:
            break
        else:
            print('Quantidade alunos acima da capacidade da classe')
    media = ((media * i) + alunos) / (i + 1)
    soma += alunos
print(f"São {soma} alunos na escola e a média de alunos por turma é de {media:2.2f}")

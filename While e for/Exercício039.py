'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno
e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.'''

alturaMaisAlto = alunoMaisAlto = alunoMaisBaixo = alturaMaisBaixo = 0

for i in range(1, 11):
    nr_aluno = int(input(f'Digite o número do aluno {i}: (1 a 10): '))
    altura = int(input(f'Digite a altura do aluno {i} em centímetros: '))
    if i == 1:
        alturaMaisAlto = altura
        alturaMaisBaixo = altura
    else:
        if altura > alturaMaisAlto:
            alunoMaisAlto = nr_aluno
            alturaMaisAlto = altura
        if altura < alturaMaisBaixo:
            alunoMaisBaixo = nr_aluno
            alturaMaisBaixo = altura

print(f'A altura do aluno mais ALTO {alturaMaisAlto}cms e o mais BAIXO {alturaMaisBaixo}cms')
print(f'O aluno mais ALTO {alunoMaisAlto} e o mais BAIXO {alunoMaisBaixo}')

    



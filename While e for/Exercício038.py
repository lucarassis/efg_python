'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:																																																		
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;																																																		
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;																																																		
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro 
do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

salario = float(input('Digite o salário inicial: R$ '))
primeiroAumento = 1.5/100
correcao_anual = 0
ano_inicio = 1995
ano_atual = 2010

for i in range(ano_inicio+1, ano_atual+1):
    ano_inicio += 1
    salario *= 1 + primeiroAumento
    primeiroAumento *=2
    print(f'Ano {i} = {salario + (salario * correcao_anual ):5.2f}')

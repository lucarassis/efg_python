'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com 
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;																																																		
b. Total de Alunos que utilizaram o sistema;																																																		
c. A Média das Notas da Turma.																																																		
																																																		
Gabarito da Prova:																																																		
																																																		
01 - A																																																		
02 - B																																																		
03 - C																																																		
04 - D																																																		
05 - E																																																		
06 - E																																																		
07 - D																																																		
08 - C																																																		
09 - B																																																		
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite
o gabarito da prova antes dos alunos usarem o programa.'''

'''print('FAÇA SUA PROVA')
gabarito = ['a','b','c','d','e','e','e','e','e','e']
gabarito2 = []
cont = acertos = total = maior = menor = 0
for i in range(1,11):
    resposta = str(input(f"{i:^2} Digite sua resposta: Questão: A, B, C, D ou E : ")).strip().upper()[0]
    gabarito2 += (gabarito)
    if i == 1 and gabarito[0]:
       cont += 1
       acertos += 1    
    elif i == 2 and gabarito[1]:
         cont += 1
         acertos += 1        
    elif i == 3 and gabarito[2]:
         cont += 1
         acertos += 1        
    elif i == 4 and gabarito[3]:
         cont += 1
         acertos += 1    
    elif i == 5 and gabarito2[4]:
         cont += 1
         acertos += 1
    elif i == 6 and gabarito[5]:
         cont += 1
         acertos += 1
    elif i == 7 and gabarito[6]:
         cont += 1
         acertos += 1
    elif i == 8 and gabarito[7]:
         cont += 1
         acertos += 1
    elif i == 9 and gabarito[8]:
         cont += 1
         acertos += 1
    elif i == 10 and gabarito[9]:
         cont += 1
         acertos += 1
    if i == 10:
        print("-="*30)
        continuar = input("Quer continuar [S-Sim] [N-Não] para sair ").strip().upper()[0]
        total += 1    
    if acertos > maior:
            maior = acertos
    if acertos < menor or acertos == 1:
            menor = acertos
print(gabarito)   
print(f'Gabarito A - {cont} de {i} E {acertos}') '''


# Iniciando as varáveis
gabarito = ''
gabarito2 = ''
count = total_acertos = total = count2 = maior = menor = 0

for e in range(1,11):
    gabarito = input(f"{e} - Digite o gabarito das notas: ").strip().upper()[0]
    gabarito2 += (gabarito)

print("-="*30)
continuar = ' '
while continuar not in 'N':

    # Zerando o Contador de acertos
    total_acertos = 0

    for c in range(1,11):
        resposta = input(f"{c} - Resposta da questao: ").strip().upper()[0]
        if c == 1 and resposta == gabarito2[0]:
            count += 1
            total_acertos += 1
        elif c == 2 and resposta == gabarito2[1]:
            count += 1
            total_acertos += 1
        elif c == 3 and resposta == gabarito2[2]:
            count += 1
            total_acertos += 1
        elif c == 4 and resposta == gabarito2[3]:
            count += 1
            total_acertos += 1
        elif c == 5 and resposta == gabarito2[4]:
            count += 1
            total_acertos += 1
        elif c == 6 and resposta == gabarito2[5]:
            count += 1
            total_acertos += 1
        elif c == 7 and resposta == gabarito2[6]:
            count += 1
            total_acertos += 1
        elif c == 8 and resposta == gabarito2[7]:
            count += 1
            total_acertos += 1
        elif c == 9 and resposta == gabarito2[8]:
            count += 1
            total_acertos += 1
        elif c == 10 and resposta == gabarito2[9]:
            count += 1
            total_acertos += 1
                
        if c == 10:
            print("-="*30)
            continuar = input("Quer continuar [N] para sair ").strip().upper()[0]
            total+=1

        if total_acertos > maior:
            maior = total_acertos
        if total_acertos < menor or total_acertos == 1:
            menor = total_acertos

print("-="*30)
print("Gabarito das respostas")
for d in gabarito2:
    count2+=1
    print(f"{count2} - {d}")
print("-="*30)

print(f"Total de acertos: {count}")
print(f"Pontos recebidos: {count}")
print(f"Maior acerto {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos a utilizar o sistema: {total}")

    

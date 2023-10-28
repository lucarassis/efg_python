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
            continuar = input("Quer continuar [S-Sim] [N-Não] para sair ").strip().upper()[0]
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
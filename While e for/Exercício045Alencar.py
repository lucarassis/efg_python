# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar 
# com o gabarito da prova e assim calcular o total de acertos e a nota 
# (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita 
# uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.

# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o professor
# digite o gabarito da prova antes dos alunos usarem o programa.
#

# Criar o gabarito da prova
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

# Criar a lista de alunos
alunos = []

# Criar a lista de acertos
acertos = []

# Criar a lista de erros
erros = []


# Criar a lista de alunos que utilizaram o sistema
alunos_utilizaram_sistema = 0

qtd_acertos = 0
qtd_erros = 0

lGabarito = int(input("Deseja alterar o gabarito? 1 - Sim, 2 - Não "))
if lGabarito == 1:
    gabarito = []
    numero_questoes = int(input("Digite o número de questões: "))
    aux = 1
    for i in range(numero_questoes):
        resp = input("Digite a questão " +  str(aux) + " do gabarito: ")
        aux += 1
        gabarito.append(resp)

opcao = 1
while opcao != 0:
    print("1 - Cadastrar respostas")
    print("3 - Listar alunos")
    print("4 - Listar médias")
    print("5 - Listar maiores acertos")
    print("6 - Listar menores acertos")
    print("7 - Listar quantidade de alunos que utilizaram o sistema")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        alunos.append(input("Digite o nome do aluno: "))

        qtd_acertos = 0
        qtd_erros = 0
        aux = 1
        for i in range(10):
            resposta = input("Digite o resposta " + str(aux) + ": ")
            aux += 1
            print("Resposta: ", resposta)
            print("Gabarito: ", gabarito[i])
            if resposta == gabarito[i]:
                qtd_acertos += 1
                print("Acertou")
            else:
                qtd_erros += 1
                print("Errou")
        nota = qtd_acertos 
        print("Acertos: ", qtd_acertos)
        print("Erros: ", qtd_erros)
        print("Nota: ", nota)   
        acertos.append(qtd_acertos)
        erros.append(qtd_erros)      

    elif opcao == 3:
        for aluno in alunos:
            print(aluno)
    elif opcao == 4:
        print("A média das notas da turma é ", sum(acertos)/len(alunos))
    elif opcao == 5:
        print("O maior acerto foi ", max(acertos))
    elif opcao == 6:
        print("O menor acerto foi ",min(acertos))
    elif opcao == 7:
        print("O sistema foi utilizado por ", len(alunos), " alunos")
    elif opcao == 0:
        print("Saindo do sistema")
    else:
        print("Opção inválida")
        exit()
        
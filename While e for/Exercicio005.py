'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.'''

mineiros = int(input('Digite a população de Mineiros: '))
jatai = int(input('Digite a população de Jataí : '))
txCrescMineiros = float(input('Digite a taxa de crescimento de Mineiros: ')) #5/100  5% de crescimento
txCrescJatai = float(input('Digite a taxa de crescimento de Jataí: ')) #1.5/100 1.5% de crescimento

ano = 0
while mineiros <= jatai:
    mineiros +=(mineiros * txCrescMineiros/100)
    jatai +=(jatai * txCrescJatai/100)
    ano += 1
    print(f'Ano {ano:>2} Mineiros {mineiros:>5.0f} e Jatai {jatai:>5.0f}')


print("levará",ano,"anos para população da cidade de Mineiros ser maior que Jatai")


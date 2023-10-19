'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

paisA = 80000
paisB = 200000
txCrescPaisA = 3/100
txCrescPaisB = 1.5/100

ano = 0
while paisA <= paisB:
    paisA +=(paisA * txCrescPaisA)
    paisB +=(paisB * txCrescPaisB)
    ano += 1
    print(f'Ano {ano:>2} Pais A {paisA:>5.0f} e pais B {paisB:>5.0f}')


print("levará",ano,"anos para população da cidade A ser maior que a cidade B")


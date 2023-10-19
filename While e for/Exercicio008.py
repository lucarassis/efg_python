#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = quant = 0 
for i in range(1,6): # i - pode ser qualquer letra, não importa no resultado.
    número = int(input(f'Digite o {i}º número: '))
    quant +=1
    soma += número

print()
print(f'A soma dos {quant} números foi de: {soma}')
print()
print(f'A média foi de {soma/quant:5.2f}')
print()
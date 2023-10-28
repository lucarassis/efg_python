'''Exercicio003: Troco: Notas e Moedas
Suponha que você seja um programador de um fabricante de máquinas de venda automática. Sua empresa quer
ajudar seus clientes dando o menor número possível de moedas como troco para cada transação. 
Simule vendas (qualquer valor). Faça um depósito de valor superior para ver o troco.
Qual é o valor é o menor número de moedas que você pode dar de troco usando
MOEDAS de 1,00; 0,50; 0,25; 0,10; 0,05 e 0,01 centavos e 
NOTAS de 2,00; 5,00; 10,00; 20,00; 50,00; 100,00 e 200,00)?'''

troco01 = 0.01
troco05 = 0.05
troco10 = 0.10
troco25 = 0.25
troco50 = 0.50
troco1_00 = 1.00
troco2_00 = 2.00
troco5_00 = 5.00
troco10_00 = 10.00
troco20_00 = 20.00
troco50_00 = 50.00
troco100_00 = 100.00
troco200_00 = 200.00

deposito = float(input('Digite o valor depositado na máquina: '))
compra = float(input('Digite o valor da compra: '))
troco = deposito - compra

print(f'\nO troco do cliente é de: {troco} \n')
#Nota 200,00
troco200_00 = int(troco / troco200_00)
troco = troco - (troco200_00*200)
#Nota 100,00
troco100_00 = int(troco / troco100_00)
troco = troco - (troco100_00 * 100.00)
#Nota 50,00
troco50_00 = int(troco / troco50_00)
troco = troco - (troco50_00 * 50.00)
#Nota 20,00
troco20_00 = int(troco / troco20_00)
troco = troco - (troco20_00 * 20.00)
#Nota 10,00
troco10_00 = int(troco / troco10_00)
troco = troco - (troco10_00 * 10.00)
#Nota 5,00
troco5_00 = int(troco / troco5_00)
troco = troco - (troco5_00 * 5.00)
#Nota 2,00
troco2_00 = int(troco / troco2_00)
troco = troco - (troco2_00 * 2.00)

print('Troco em Notas')
print(f'{troco200_00} Nota de 200,00 \n{troco100_00} Nota de 100,00 \n{troco50_00} Nota de 50,00 \n{troco20_00} Nota de 20,00 \n{troco10_00} Nota de 10,00\n{troco5_00} Nota de 5,00 \n{troco2_00} Nota de 2,00')

print('\nEm Moedas')
#moeda de 1.00
troco100 = int(troco)
troco = troco - (troco100 * 1)
#moeda de 0.50
troco50 = int(troco / troco50)
troco = troco - (troco50 * 0.5)
#moeda de 0.25
troco25 = int(troco / troco25)
troco = troco - (troco25 * 0.25)
#moeda de 0.10
troco10 = int(troco / troco10)
troco = troco - (troco10 * 0.10)
#troco de 0.05
troco05 = int(troco / troco05)
troco = troco - (troco05 * 0.05)
#troco de 0.01
troco01 = troco * 100

print(f'{troco100} Moeda de 1,00\n{troco50} Moeda de 0,50\n{troco25} Moeda de 0,25\n{troco10} Moeda de 0,10\n{troco05} Moeda de 0,05\n{troco01:.0f} Moeda de 0,01')

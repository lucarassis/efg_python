'''Exercicio002: Troco: Moedas
Suponha que você seja um programador de um fabricante de máquinas de venda automática. Sua empresa quer
ajudar seus clientes dando o menor número possível de moedas como troco para cada transação. 
Suponha que um cliente coloca em uma nota de 2,00 e compra um ítem por 0,37. Qual é o valor é o
menor número de moedas que você pode dar de troco (usando moedas de 1,00; 0,50; 0,25; 0,10; 0,05 e 0,01
centavos)? 
REGRA inicial da máquina, ela só devolve o troco em moedas, mas aceita moedas de 1,00 e notas de 2,00;
5,00 e 10,00.'''

nota1 = 1.00
nota2 = 2.00
nota5 = 5.00
nota10 = 10.00

troco01 = 0.01
troco05 = 0.05
troco10 = 0.10
troco25 = 0.25
troco50 = 0.50
troco100 = 1.00

deposito = float(input('Digite o valor depositado na máquina: '))
compra = float(input('Digite o valor da compra: '))
troco = deposito - compra

print(f'O troco do cliente é de: {troco}')
#moeda de 1.00
troco100 = int(troco)
troco = troco - troco100
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


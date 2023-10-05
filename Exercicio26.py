'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte 
forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da 
gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

abastecimento = int(input('Digite quantos litros vai abastecer: '))
tipoCombustivel = str(input("Qual tipo de combustível (G-Gasolina E-Etanol): "))
gasolina = 2.50
etanol = 1.90

if tipoCombustivel == "G" or tipoCombustivel == "g":
    if abastecimento > 20:
        desconto = (gasolina * 6/100) * abastecimento
        print(f'Valor a pagar: {gasolina * abastecimento - desconto:5.2f}')
    else:
        desconto = (gasolina * 4/100) * abastecimento
        print(f'Valor a pagar: {gasolina * abastecimento - desconto:5.2f}')

if tipoCombustivel == "E" or tipoCombustivel == "e":
    if abastecimento > 20:
        desconto = (etanol * 5/100) * abastecimento
        print('Valor a pagar:', round(etanol * abastecimento - desconto,2))
    else:
        desconto = (etanol * 3/100) * abastecimento
        print('Valor a pagar:', round(etanol * abastecimento - desconto,2))



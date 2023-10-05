'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

kgMorangos = int(input('Digite quantos Kg de morangos: '))
kgMaca = int(input('Digite quantos Kg de Maças: '))
totalKg = kgMorangos + kgMaca

if kgMorangos > 5:
    totalmorangos = 0
    morango5 = 2.2
    totalmorangos += kgMorangos * morango5
    print(f'Você comprou {kgMorangos * morango5:5.2f} de morangos')
else:
    totalmorangos = 0
    morango = 2.5
    totalmorangos += kgMorangos * morango
    print(f'Você comprou {kgMorangos * morango:5.2f} de morangos')
    
if kgMaca > 5:
    totalmaca = 0
    maca5 = 1.5
    totalmaca += kgMaca * maca5
    print(f'Você comprou {kgMaca * maca5:5.2f} de maças')
else:
    totalmaca = 0
    maca = 1.8
    totalmaca += kgMaca * maca
    print(f'Você comprou {kgMaca * maca:5.2f} de maças')
    
if kgMaca + kgMorangos > 8 or totalmorangos + totalmaca > 25:
    print(f'O preço final é de {(totalmorangos + totalmaca) * .9:5.2f}, considerando desconto de 10% no preço final')
else:
    print(f'O preço final é de {totalmorangos + totalmaca:5.2f}')
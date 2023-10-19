print('{:=^40}'.format(' Loja LUCARASSIS '))
preço = float(input('Preço da compra: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista din/ch - 10% desc
[ 2 ] à vista no cartão - 5% desc
[ 3 ] 2X no cartão - S/ Juros
[ 4 ] 3X ou até 10x no cartão + 20% acrésc ''')
opção = int(input('Qual sua opção de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcela em 2x de R$: {parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparcela = int(input('Em quantas parcelas? [ 3 A 10 ] '))
    parcela = total / totparcela
    print(f'Sua compra será parcelada em {totparcela}x de R$: {parcela:.2f}')
print(f'Sua compra de R$ {preço:.2f} vai custar R$: {total:.2f}')
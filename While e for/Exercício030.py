'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, 
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

Preço do pão: R$ 0.18																																																		
Panificadora Pão de Ontem - Tabela de preços																																																		
1 - R$ 0.18																																																		
2 - R$ 0.36																																																		
...																																																		
50 - R$ 9.00'''		

precoDoPao = float(input("Digite o valor unitário do pão R$ " ))
quant = 0
for i in range(1,51):
    print(f'{i:2.0f} X {precoDoPao:2.2f} = {i * precoDoPao:2.2f}')

quant = int(input('Digite quantos ítens o cliente tem na cesta: '))
if quant < 51:
    print('*'*60)
    print(f'O cliente comprou {quant} pães. \nValor total da compra R$: {quant * precoDoPao:2.2f}')
    print('*'*60)
else:
    print('Quantidade acima do permite por cliente')

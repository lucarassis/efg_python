'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:																																																		
																																																		
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida																																																		
1       0																																																		
3       10																																																		
6       15																																																		
9       20																																																		
12      25																																																		
																																																	
Exemplo de saída do programa:																																																		
																																																		
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela																																																		
R$ 1.000,00     0               1                       R$  1.000,00																																																		
R$ 1.100,00     100             3                       R$    366,00																																																		
R$ 1.150,00     150             6                       R$    191,67'''

vr_divida = float(input("Digite o valor da dívida: "))
parcelas = 1
juros = 0
print(
    "|Valor da Dívida|Valor dos Juros|Qtde  Parcelas |Valor da Parcela|"
)
while True:
    juros = (5 / 3) * parcelas + 5 # a cada 3 meses, aumenta 5%
    if parcelas == 1:
        juros = 0

    vr_juros = vr_divida * (juros / 100)
    vr_total = vr_divida + vr_juros
    vr_parcela = vr_total / parcelas
    print(
        f"|R$ {vr_total:.2f}\t"
        f"|R$ {vr_juros:.2f}\t"
        f"|{parcelas}\t\t"
        f"|R$ {vr_parcela:.2f}"
    )
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    if parcelas > 12:
        break


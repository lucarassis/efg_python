'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''
ValorHora = float(input('Digite o valor da hora trabalhada R$: '))
QdeHoraTrabalhada = float(input('Digite a quantidade horas trabalhadas no mês: '))
SalarioBruto = ValorHora * QdeHoraTrabalhada

if SalarioBruto <= 900:
    DescIR = 0
elif SalarioBruto <=1.500:
    DescIR = 5
elif SalarioBruto <= 2.500:
    DescIR = 10
else:
    DescIR = 20
IR = SalarioBruto * (DescIR / 100)
INSS = SalarioBruto * (10 / 100)
Sindicato = SalarioBruto * (3 / 100)
FGTS = SalarioBruto * (11 / 100)
DescontosFolha = IR + INSS + Sindicato
SalarioLiquido = SalarioBruto - DescontosFolha

print(
    f'\n Salário Bruto : R$ {SalarioBruto:5.2F}',
    F'\n ( - ) IR {DescIR} : R$ {IR:5.2f}',
    f'\n ( - ) INSS (10%): R$ {INSS:5.2f}'
    f'\n ( - ) Sindicato: R$ {Sindicato:5.2f}'
    f'\n FGTS (11%) : R$ {FGTS:5.2f}'
    f'\n Descontos Folha : R$ {DescontosFolha:5.2f}'
    f'\n Salário Líquido : R$ {SalarioLiquido:5.2f}'
)


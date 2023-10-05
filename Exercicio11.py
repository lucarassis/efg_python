'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salarioAnterior = float(input('Digite seu salário R$: '))
salarioAposAumento = 0
diferencaSalarial = 0
percentualDeAumento = 0

if salarioAnterior <= 280:
    percentualDeAumento = 20
elif salarioAnterior <= 700:
    percentualDeAumento = 15
elif salarioAnterior <= 1500:
    percentualDeAumento = 10
else:
    percentualDeAumento = 5

diferencaSalarial = salarioAnterior * (percentualDeAumento / 100)
salarioAposAumento = salarioAnterior + diferencaSalarial

print(f'Seu salário antes do reajuste era de R$ {salarioAnterior:5.2F}')
print(f'Seu salário foi aumentado em {percentualDeAumento}%')
print(f'O valor do aumento em seu salário foi de R$ {diferencaSalarial:5.2f}')
print(f'Seu novo salário, após o aumento é de R$ {salarioAposAumento:5.2f}')
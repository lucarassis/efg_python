#Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

from time import sleep
def maior(* núm):
    cont = maior = 0
    print("Analisando os valores digitados...")
    for valor in núm:
        print(f'{valor}', end=" - ", flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram encontrados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(numero1, numero2, numero3)

# aprendi com professor Guanabara
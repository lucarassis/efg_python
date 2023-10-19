"""Altere o programa de cálculo dos números primos, 
informando, caso o número não seja primo, por quais número ele é divisível."""

numero = int(input("Digite um numero inteiro: "))
primo = True
for i in range(1, numero):
    if numero % i == 0:
        primo = False
        print(f"{i}", end=' - ')
print(f'{numero}')
if primo: 
    print(f"{numero} é primo!")

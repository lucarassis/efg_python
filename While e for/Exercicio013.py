'''Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.'''

base = int(input('Digite a base da potência: '))
expoente = int(input('Digite o expoente da potência: '))

resultado = 1
for i in range (expoente):
    resultado = resultado * base
print(resultado)


#para ver se deu certo, na fórmula do python

print(f'Este é o resultado da função expoente {base ** expoente}')



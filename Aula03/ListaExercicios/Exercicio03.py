#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite F ou M: ')

if sexo == "F" or sexo == "f":
    print('F - Feminino')
elif sexo == 'M' or sexo == "m":
    print('M - Masculino')
else:
    print('Sexo inválido')
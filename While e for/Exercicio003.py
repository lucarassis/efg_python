'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = input('Digite seu nome. Mínimo 3 caracteres: ')
while len(nome) <3:
    print('Quantidade de letras inferior ao solicitado.')
    if len(nome) <3:
        nome = input("Digite seu nome: ")

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    print('Idade inválida')
    if idade < 0 or idade > 150:
        idade = int(input('Digite sua idade: '))
    
sexo = input('Digite (F - Feminino M - Masculino): ')
while  sexo !="F" and sexo!="M" :
	sexo=str(input("informe a inicial do seu sexo: (F ou M) "))
	
estado_civil=str(input("informe a inicial do seu estado civil: "))
while ( estado_civil != "S" and estado_civil != "C" and estado_civil != "S" and estado_civil != "D" ):
	estado_civil=str(input("informe a inicial do seu estado civil: "))


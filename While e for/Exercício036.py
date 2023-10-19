'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final 
devem ser informados também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5																																																		
Começar por: 4																																																		
Terminar em: 7																																																		
																																																		
Vou montar a tabuada de 5 começando em 4 e terminando em 7:																																																		
5 X 4 = 20																																																		
5 X 5 = 25																																																		
5 X 6 = 30																																																		
5 X 7 = 35																																																		
																																																		
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.	'''

tabuada = int(input('Digite um número para pesquisar na tabuada: De 1 a 10: '))
ini = int(input('Digite qual número deseja começar sua tabuada entre 1 e 10: '))
fim = int(input('Digite o segundo número da tabuada, sempre acima do primeiro número e no máximo até 10: '))

if fim < ini:
    fim = int(input('Você digitou um número MENOR que o inicial. Favor digitar um número SUPERIOR: '))
for i in range (ini, fim+1):
    print(f'{tabuada:2.0f} x {i:2.0f} = {tabuada*i:2.0f}')

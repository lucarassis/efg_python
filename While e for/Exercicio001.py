'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido.'''

nota = float(input('Digite uma nota: '))
while 0 > nota or 10 < nota:
	nota =float(input("informe um numero de 0 a 10: "))

'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e 
voltando a pedir as informações.'''

print()
print("faça já seu cadastro:")
usuario=str(input("Digite seu nome de usuário: "))
senha=str(input("Digite sua senha: "))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("Digite novamente seu nome de usuário: "))
	senha=str(input("Digite novamente sua senha, diferente da senha anterior: "))
else:
	print("Seu cadastrado foi efetuado com sucesso.")


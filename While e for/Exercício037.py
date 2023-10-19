'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes
da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, 
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.'''

cod_clientes = []
cod_altura = []
cod_peso = []
n_cliente = 1
codigo = True

while codigo != 0:
    print("\nCliente n° ", n_cliente)
    codigo = int(input("Digite 0 para finalizar ou Digite o código do cliente: "))
    if codigo == 0:
        break
    else:
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        cod_clientes.append(codigo)
        cod_altura.append(altura)
        cod_peso.append(peso)
        n_cliente += 1

cod_magro = cod_peso.index(min(cod_peso))
cod_gordo = cod_peso.index(max(cod_peso))
cod_alto = cod_altura.index(max(cod_altura))
cod_baixo = cod_altura.index(min(cod_altura))
print("*" * 60)
print("Código do mais magro: ", cod_clientes[cod_magro])
print("Código do mais gordo: ", cod_clientes[cod_gordo])
print("Código do mais alto: ", cod_clientes[cod_alto])
print("Código do mais baixo: ", cod_clientes[cod_baixo])
print("Média de altura: ", round(sum(cod_altura) / len(cod_altura),2))
print("Média de peso: ", round(sum(cod_peso) / len(cod_peso),2))
print("*" * 60)
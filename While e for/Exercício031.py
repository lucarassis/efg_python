'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 																																																		
Produto 1: R$ 2.20																																																		
Produto 2: R$ 5.80																																																		
Produto 3: R$ 0																																																		
Total: R$ 9.00																																																		
Dinheiro: R$ 20.00																																																		
Troco: R$ 11.00																																																		
...		'''

while True:
    print('LOJA TABAJARA')
    n = 1
    total = 0

    while True:
        preco = float(input(f"Produto {n:2.0f} - R$: "))
        n += 1
        total += preco
        if preco == 0:
            break

    print("*"*60)

    print(f"Total: R$ {total:.2f} ")
    dinheiro = float(input('Dinheiro: R$ '))
    print(f"Troco: R$ {dinheiro - total:2.2f}")

    print("*"*60)

    reset = input("Pressione 1 para nova compra ou 2 para finalizar a compra: ")
    if reset == "1":
        continue
    else:
        print("Compra finalizada com sucesso")
        break



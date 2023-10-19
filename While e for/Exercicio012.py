'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''

tabuada = int(input('Digite um número para pesquisar na tabuada: De 1 a 10: '))

for i in range (1,11):
    print(f'{tabuada:2.0f} x {i:2.0f} = {tabuada*i:2.0f}')
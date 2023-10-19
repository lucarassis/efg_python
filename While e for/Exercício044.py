'''Em uma eleição presidencial existem quatro candidatos. 
Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 																																																		
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)																																																		
5 - Voto Nulo																																																		
6 - Voto em Branco																																																		
																																																		
Faça um programa que calcule e mostre:																																																		
O total de votos para cada candidato;																																																		
O total de votos nulos;																																																		
O total de votos em branco;																																																		
A percentagem de votos nulos sobre o total de votos;																																																		
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.'''

print('''
=====================
| COD | Candidato   | 
|  1  | José        |
|  2  | João        |
|  3  | Antônio     |
|  4  | Lucas       |
|  5  | Nulo        |
|  6  | Branco      |
|  0  | Finalizar   |
=====================
Para sair digite 0''')

Candidatos = {
    '1': ['José', 1],
    '2': ['João', 1],
    '3': ['Antônio', 1],
    '4': ['Lucas', 1],
    '5': ['Nulo', 1],
    '6': ['Branco', 1],
}
voto = {}
while True:
    codigo = input('Informe o codigo do candidato: ')
    if (codigo == '0'):
        break
    

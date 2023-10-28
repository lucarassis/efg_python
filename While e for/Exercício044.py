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
====================
| COD | Candidato  | 
|  1  | José       |
|  2  | João       |
|  3  | Antônio    |
|  4  | Lucas      |
|  5  | Nulo       |
|  6  | Branco     |
====================
Para sair digite 0''')

cand1 = cand2 = cand3 = cand4 = cand5 = cand6 = 0
while True:
    voto = int(input('Digite o número de seu candidato ou para finalizar: '))
    if voto == 0:
        break
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        cand5 += 1
    elif voto == 6:
        cand6 += 1
    else: 
            print('Voto inválido. Escolha seu candidato, nulo ou branco. Até número 6: ')
votantes = cand1 + cand2 + cand3 + cand4 + cand5 + cand6
print('='*55)
print(f'Total de votantes: {votantes}')
print(f'Voto José   : {cand1} corresponde a {cand1/votantes*100:.2f}%')
print(f'Voto João   : {cand2} corresponde a {cand2/votantes*100:.2f}%')
print(f'Voto Antônio: {cand3} corresponde a {cand3/votantes*100:.2f}%')
print(f'Voto Lucas  : {cand4} corresponde a {cand4/votantes*100:.2f}%')
print(f'Voto Nulo   : {cand5} corresponde a {cand5/votantes*100:.2f}%') 
print(f'Voto Branco : {cand6} corresponde a {cand6/votantes*100:.2f}%')
print('='*55)   
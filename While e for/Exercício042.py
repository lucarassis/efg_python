'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão 
nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

n = 1
c1 = c2 = c3 = c4 = 0 
while n> 0:
    n =int(input("Digite um número: "))
    if n>= 0 and n<= 25:
        c1 += 1
    elif n>= 26 and n<= 50:
        c2 += 1
    elif n>= 51 and n<= 75:
        c3 += 1
    elif n>= 76 and n<= 100:
        c4 += 1
print('-'*25)
print(f'''A quantidade de números:  
entre   0-25 : {c1} voto(s)
entre  26-50 : {c2} voto(s)
entre  51-75 : {c3} voto(s)
entre 76-100 : {c3} Voto(s)''')
print('-'*25)

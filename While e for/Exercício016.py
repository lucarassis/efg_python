'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.'''

n0 = 0
n1 = 0

while (n1 < 611):
    print(n1)
    n1 = n1 + n0
    n0 = n1 - n0

    if (n1 == 0):
        n1 += 1
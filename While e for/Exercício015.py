'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.'''

num = 1
num_ant = 0
for _ in range(int(input('Digite o numero de termos da série de Fibonacci: '))):
    print(num)
    aux = num
    num += num_ant
    num_ant = aux
print(f'O numéro final da série de Fibonacci é: {aux}')
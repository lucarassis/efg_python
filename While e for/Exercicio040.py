'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
a. Código da cidade;																																																		
b. Número de veículos de passeio (em 1999);																																																		
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:																																																		
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;																																																		
e. Qual a média de veículos nas cinco cidades juntas;																																																		
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''	
																																																	
nr_veiculos = nr_acidentes = soma = media = quant = somaveiculos = maiorNrAcidentes = menorNrAcidentes = 0
maiorCidAcid = menorCidAcid = quantCidMenores= 0

for i in range(1,6):
    cod_cidade = int(input(f'Digite o código da cidade {i}: '))
    nr_veiculos = int(input(f'Digite quantos veículos a cidade {cod_cidade} possui : '))
    nr_acidentes = int(input(f'Digite quantos acidentes ocorreu na cidade {cod_cidade}: '))
    
    if i == 1:
        maiorNrAcidentes = nr_acidentes
        maiorCidAcid = cod_cidade
        menorNrAcidentes = nr_acidentes
        menorCidAcid = cod_cidade
    else:
        if nr_acidentes > maiorNrAcidentes:
            maiorNrAcidentes = nr_acidentes
            maiorCidAcid = cod_cidade
        if nr_acidentes < menorNrAcidentes:
            menorNrAcidentes = nr_acidentes
            menorCidAcid = cod_cidade 

    if nr_veiculos < 2000:
        quantCidMenores += 1
        quant += 1
        soma += nr_acidentes
        somaveiculos += nr_veiculos
    else:
        quant +=1
        somaveiculos += nr_veiculos
media = somaveiculos / quant
print('-'*90)
print(f'O MAIOR número de acidentes: {maiorNrAcidentes} Cidade {maiorCidAcid} e o MENOR número de acidentes: {menorNrAcidentes} Cidade {menorCidAcid}')
print(f'A média de veículos nas cidades são: {media:2.0f} veículos')
print(f'Acidentes em cidades menores que 2000 habitantes são: {soma} que dão em média: {soma/quantCidMenores:2.2f}')
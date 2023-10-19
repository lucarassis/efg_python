'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

candA = candB = candC = cont = 0
 
for eleitores in range(1, int(input('digite quantos eleitores existem nesta seção: '))+1):
    voto = str(input(
        "Digite o seu candidato (candA - candB - candC): em quem o "
        f"eleitor {eleitores} quer votar: "))

    if voto == "candA":
        candA += 1
    if voto == "candB":
        candB += 1
    if voto == "candC":
        candC += 1
print(
    "Votação encerrada"
    f"\nCandidato A: {candA} voto(s)"
    f"\nCandidato B: {candB} voto(s)"
    f"\nCandidato C: {candC} voto(s)"
)
print(f' {eleitores} votantes na seção')

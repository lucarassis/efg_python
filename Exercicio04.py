#Faça um programa que verifique se uma letra digitada é vogal ou consoante

vogal = input("Digite uma letra do alfabeto, forma minuscula: ")

if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
    print('A letra digitada é uma vogal')
elif vogal != ('a', 'e', 'i', 'o', 'u'):
    print('A letra digitada é uma consoante')
else:
    print("Esta letra não foi digitada na forma solicitada")

    

# professor vai refazer, aguarde.
import os
print('Bem vindo ao Jogo da Forca')
palavra_secreta=input('Digite a Palavra: ').upper()
n_tentativas=int(input('Digite quantas tentativas: '))
tentativas=0
os.system('cls')
linhas = ['_'] * len(palavra_secreta)
print('adivinhe a palavra')
print(f'A palavra tem {len(palavra_secreta)} caracteres')
while ( "_" in linhas):
    entrada=input('Digite uma letra: ').upper()
    letra_igual=False
    if(entrada == palavra_secreta):
            break
    for i in range(0,len(palavra_secreta)):
        if(entrada == palavra_secreta[i]):
            linhas[i] = entrada.upper()
            letra_igual=True
    if (letra_igual == False):
        tentativas +=1
        print(f'Você tem {n_tentativas - tentativas} tentativas restantes')
    print(linhas)                
    if(tentativas == n_tentativas):
        print('Você esgotou as tentativas, fim de jogo')
        break
if(n_tentativas != tentativas):
    print('Parabens Você Ganhou !')           

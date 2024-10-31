#biblioteca para limpar a tela
import os

#configuracao adivinha
stringA = input("Digite a palavra:")
stringA = stringA.upper() #na tabela ascii letras minusculas e maiusculas sao case sensitive
tamanho_string = len(stringA)
numero_max_tentativas = int(input("Digite o número máximo de tentativas:"))

os.system('clear')
print(f"voce tem:{numero_max_tentativas} tentativas")
estado = False
tentativa = 0

#separando as strings in caracteres individuais
lst = []
for letter in stringA:
    lst.append(letter)

#array auxiliar (preencher a string)
stringB = ['_'] * tamanho_string #vai preencher o vetor com espaço do mesmo tamanho da stringA
                                #preenche o vetor

#jogo
while(tentativa < numero_max_tentativas):
    entrada = input("Digite um caractere ou uma string:")
    entrada = entrada.upper()

    if(stringA == entrada) or (estado == True): # o erro está nesse loop aqui, ele pula o restante da verificação esse loop más continua
        print(f"Parabéns, você ganhou em, {tentativa}, tentativas")
        break

    elif(len(entrada) == 1):
        for i in range(0,tamanho_string):
            if(entrada == stringA[i]):
                stringB[i] = entrada.upper()
    
    if(lst == stringB):
        estado = True
    
    print(estado)
    print(stringB)

    tentativa += 1

if(tentativa == numero_max_tentativas):
    print("Que pena. A palavra éra:",stringA)
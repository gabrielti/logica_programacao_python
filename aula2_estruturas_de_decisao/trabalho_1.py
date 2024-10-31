#-------------------------------------------------
#program_name: trabalho_1
#authors: Wellington Costa, Gabriel Takiguchi, Pedro Melo, Murilo Trippia 
#data: 26/03/24
#version: 1.0
#objective: game
#-------------------------------------------------


#bibliotecas
import random
import time

#requisito numero jogadores
print("1 - individual")
print("2 - dupla")
numero_jogadores = int(input("opcao:"))

print(" ")

#requisito dificuldade
print("nivel:")
print("3 - facil")
print("4 - medio")
print("5 - dificil")
dificuldade = int(input("opcao:"))

print(" ")

#range de numeros de acordo com a dificuldade
if(dificuldade == 3):

    r1 = -10
    r2 = 10

    numero_1 = random.randrange(r1,r2)
    numero_2 = random.randrange(r1,r2)

if(dificuldade == 4): #elif

    r1 = -100
    r2 = 100

    numero_1 = random.randrange(r1,r2)
    numero_2 = random.randrange(r1,r2)

if(dificuldade == 5): #else (nao necessariament cada if precisa de um else)

    r1 = -1000
    r2 = 1000

    numero_1 = random.randrange(r1,r2)
    numero_2 = random.randrange(r1,r2)



#jogador1 - individual
        
#soma
sum = numero_1+numero_2
print(numero_1, "+",numero_2, "=", "?")

tempo_exe = time.time()

resposta = int(input("?:"))

tempo_exe = time.time() - tempo_exe

#soma_analise_tempo
print("tempo_exe:",tempo_exe)

if(tempo_exe > 30):
    ponto = 0
    
else:
    if(resposta == sum and tempo_exe <= 5):
        ponto = 10
        
    elif(resposta == sum and 5<tempo_exe<=30):
        ponto = 10 - int(tempo_exe-5)*0.2
        
    else:
        ponto = 0

print("pontuacao:",ponto,"\n")
    
#subtracao
numero_1 = random.randrange(r1,r2)
numero_2 = random.randrange(r1,r2)
            
sub = numero_1-numero_2
print(numero_1, "-",numero_2, "=", "?")

tempo_exe = time.time()

resposta = int(input("?:"))

tempo_exe = time.time() - tempo_exe

#subtracao_analise_tempo
print("tempo_exe:",tempo_exe)

if(tempo_exe > 30): #colocar ou, or
    ponto = ponto + 0
    
else: #poderia usar um elif
    if(resposta == sub and tempo_exe <= 5):
        ponto = ponto + 10
        
    elif(resposta == sub and 5<tempo_exe<=30):
        ponto = ponto + (10 - int(tempo_exe-5)*0.2)
        
    else:
        ponto = ponto + 0
    
print("pontuacao:",ponto,"\n")

#multiplicacao
numero_1 = random.randrange(r1,r2)
numero_2 = random.randrange(r1,r2)

mult = numero_1*numero_2
print(numero_1, "*",numero_2, "=", "?")

tempo_exe = time.time()

resposta = int(input("?:"))

tempo_exe = time.time() - tempo_exe

#mult_analise_tempo
print("tempo_exe:",tempo_exe)

if(tempo_exe > 30):
    ponto = ponto + 0
    
else:
    if(resposta == mult and tempo_exe <= 5):
        ponto = ponto + 10
        
    elif(resposta == mult and 5<tempo_exe<=30):
        ponto = ponto + (10 - int(tempo_exe-5)*0.2)
        
    else:
        ponto = ponto + 0

print("pontuacao:",ponto,"\n")   

    #divisao inteiro
numero_1 = random.randrange(r1,r2)
numero_2 = random.randrange(r1,r2)

div = int(numero_1/numero_2)
print(numero_1, "//",numero_2, "=", "?")

tempo_exe = time.time()

resposta = int(input("?:"))

tempo_exe = time.time() - tempo_exe

#div_analise_tempo
print("tempo_exe:",tempo_exe)

if(tempo_exe > 30):
    ponto = ponto + 0
    
else:
    if(resposta == div and tempo_exe <= 5):
        ponto = ponto + 10
        
    elif(resposta == div and 5<tempo_exe<=30):
        ponto = ponto + (10 - int(tempo_exe-5)*0.2)
        
    else:
        ponto = ponto + 0

    print("pontuacao:",ponto,"\n")   

#2 jogador
if(numero_jogadores == 2):

    print("\n jogador2")
    
    #soma
    sum = numero_1+numero_2
    print(numero_1, "+",numero_2, "=", "?")

    tempo_exe = time.time()

    resposta = int(input("?:"))

    tempo_exe = time.time() - tempo_exe

    #soma_analise_tempo
    print("tempo_exe:",tempo_exe)

    if(tempo_exe > 30):
        ponto_2 = 0
    
    else:
        if(resposta == sum and tempo_exe <= 5):
            ponto_2 = 10
        
        elif(resposta == sum and 5<tempo_exe<=30):
            ponto_2 = 10 - int(tempo_exe-5)*0.2
        
        else:
            ponto_2 = 0

    print("pontuacao:",ponto_2,"\n")
    
    #subtracao
    numero_1 = random.randrange(r1,r2)
    numero_2 = random.randrange(r1,r2)
            
    sub = numero_1-numero_2
    print(numero_1, "-",numero_2, "=", "?")

    tempo_exe = time.time()

    resposta = int(input("?:"))

    tempo_exe = time.time() - tempo_exe

    #subtracao_analise_tempo
    print("tempo_exe:",tempo_exe)

    if(tempo_exe > 30):
        ponto_2 = ponto_2 + 0
    
    else:
        if(resposta == sub and tempo_exe <= 5):
            ponto_2 = ponto_2 + 10
        
        elif(resposta == sub and 5<tempo_exe<=30):
            ponto_2 = ponto_2 + (10 - int(tempo_exe-5)*0.2)
        
        else:
            ponto_2 = ponto_2 + 0
    
    print("pontuacao:",ponto_2,"\n")

    #multiplicacao
    numero_1 = random.randrange(r1,r2)
    numero_2 = random.randrange(r1,r2)

    mult = numero_1*numero_2
    print(numero_1, "*",numero_2, "=", "?")

    tempo_exe = time.time()

    resposta = int(input("?:"))

    tempo_exe = time.time() - tempo_exe

    #mult_analise_tempo
    print("tempo_exe:",tempo_exe)

    if(tempo_exe > 30):
        ponto_2 = ponto_2 + 0
    
    else:
        if(resposta == mult and tempo_exe <= 5):
            ponto_2 = ponto_2 + 10
        
        elif(resposta == mult and 5<tempo_exe<=30):
            ponto_2 = ponto_2 + (10 - int(tempo_exe-5)*0.2)
        
        else:
            ponto_2 = ponto_2 + 0

    print("pontuacao:",ponto_2,"\n")   

    #divisao inteiro
    numero_1 = random.randrange(r1,r2)
    numero_2 = random.randrange(r1,r2)

    div = int(numero_1/numero_2)
    print(numero_1, "//",numero_2, "=", "?")

    tempo_exe = time.time()

    resposta = int(input("?:"))

    tempo_exe = time.time() - tempo_exe

    #div_analise_tempo
    print("tempo_exe:",tempo_exe)

    if(tempo_exe > 30):
        ponto_2 = ponto_2 + 0
    
    else:
        if(resposta == div and tempo_exe <= 5):
            ponto_2 = ponto_2 + 10
        
        elif(resposta == div and 5<tempo_exe<=30):
            ponto_2 = ponto_2 + (10 - int(tempo_exe-5)*0.2)
        
        else:
            ponto_2 = ponto_2 + 0

    print("pontuacao:",ponto_2,"\n")

    if(ponto > ponto_2):
        print("jogador 1 ganhou!")

    elif(ponto == ponto_2):
        print("empate!")

    else:
        print("jogador 2 ganhou!")


    





import random 

linhas = 7
colunas = 5

matriz = []

#preenchimento da matriz
for i in range(linhas):

    matriz_suporte = []

    for j in range(colunas):
        numero = random.randrange(10)
        matriz_suporte.append(numero)
    
    matriz.append(matriz_suporte)

#impressao da matriz
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j],end = '')
    print()


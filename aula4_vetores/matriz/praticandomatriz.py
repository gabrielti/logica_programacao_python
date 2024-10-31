linhas = int(input("numero de linhas:"))
colunas = int(input("numero de colunas:"))

matriz = []

#preenchimento da matriz
for i in range(linhas):

    matriz_suporte = []

    for j in range(colunas):
        numero = int(input("digite um inteiro:"))
        matriz_suporte.append(numero)
    
    matriz.append(matriz_suporte)

#impressao da matriz
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j],end = '')
    print()

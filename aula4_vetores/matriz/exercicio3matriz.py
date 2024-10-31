import random

linhas = 4
colunas = 4

count = 0
soma = 0
soma2 = 0

matriz = []

#preenchimento da matriz
for i in range(linhas):

    matriz_suporte = []

    for j in range(colunas):
        numero = random.randrange(10)

        if i == j:
            soma = soma+numero
            count += 1

        if (i+j) == 3:
            soma2 = soma2+numero

        matriz_suporte.append(numero)

    matriz.append(matriz_suporte)

#impressao da matriz
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j],end = '')
    print()
print("soma:",soma)

media_diagonal_principal = soma/count
media_diagonal_secundaria = soma2/count


print(f"media diagonal principal:{media_diagonal_principal}")
print(f"media diagonal secundaria:{media_diagonal_secundaria}")

import random

matriz = []

#popula matriz com 9 numeros randomicos de 0 a 10
for i in range(3):

    array = []

    for j in range(3):
        numero = random.randrange(10)
        array.append(numero)

    matriz.append(array)

#imprime matriz com formatacao correta
for i in range(3):
    
    for j in range(3):
        print(matriz[i][j],end='')
    print()

import random

matriz = []


#populando a matriz 7x5 com elementos aleatorios de valor variando entre 0 e 9
for i in range(7):
    
    array = []

    for j in range(5):
        numero = random.randrange(9)
        array.append(numero)

    matriz.append(array)


#imprimir a matriz
for i in range(7):
    for j in range(5):
        print(matriz[i][j],end = '')
    print()

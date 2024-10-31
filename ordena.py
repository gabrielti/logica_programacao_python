import random

array = []

#preenche matriz
for i in range(10):
    numero = random.randrange(10)
    array.append(numero)

print("array:",array)

#ordena matriz
size = 9
while(size > 0):
    for j in range(size):
        if array[j] > array[j+1]:
            aux = array[j+1]
            array[j+1] = array[j]
            array[j] = aux
    size -= 1

print("array ordenado:",array)


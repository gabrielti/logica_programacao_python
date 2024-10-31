import random

size = int(input("vector size:"))
vector = []

for i in range(size):
    number = random.randrange(100)
    vector.append(number)

for j in range(size):

    if j == 0:
        print(f"            current:{vector[j]} forward:{vector[j+1]}")

    elif (j+1) == size:
        print(f"backward:{vector[j-1]} current:{vector[j]}")
        #nao precisa do break porque quando for j+1 == size
        #ja estara na ultima posicao do vetor, lembrando que essa funcao
        #em python, o j nunca chega ate size. Ele alcance no maximo size-1
        #igual na matematica, j nao inclui size. é um exludente

    else:
        print(f"backward:{vector[j-1]} current:{vector[j]} forward:{vector[j+1]}")


print("vector:",vector)

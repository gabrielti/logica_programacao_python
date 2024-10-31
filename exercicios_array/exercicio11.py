import random

tamanho_vetor = int(input("tamanho do vetor:"))
vetor = []

for i in range(tamanho_vetor):
    numero = random.randrange(100)
    vetor.append(numero)
    maior = vetor[0]

for j in range(tamanho_vetor):

    if(vetor[j] > maior):
        maior = vetor[j]

print(vetor)
print("maior numero no vetor:",maior)


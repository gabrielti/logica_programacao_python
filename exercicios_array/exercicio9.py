import random
vetor1 = []
vetor2 = []
soma = []

for i in range(5):
    numero = random.randrange(10)
    vetor1.append(numero)
    
    numero = random.randrange(10)
    vetor2.append(numero)

for j in range(5):
    soma_numero = vetor1[j] + vetor2[j]
    soma.append(soma_numero)

print(vetor1)
print(vetor2)
print(soma)

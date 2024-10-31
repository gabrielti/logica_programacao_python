import random
vetor = []
controlador = 99

for i in range(100):
    numero = random.randrange(100)
    vetor.append(numero)

for j in range(50):
    soma = vetor[j]+vetor[controlador]
    print(f"vetor[{j}] + vetor[{controlador}] = {soma}")
    controlador -= 1 

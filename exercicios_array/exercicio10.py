import random
vetor = []
sub_vetor_1 = []
sub_vetor_2 = []
controlador = 10

for i in range(20):
    numero = random.randrange(10)
    vetor.append(numero)

for j in range(10):
    sub_vetor_1.append(vetor[j])
    sub_vetor_2.append(vetor[controlador])
    controlador += 1

print(vetor)
print(sub_vetor_1)
print(sub_vetor_2)

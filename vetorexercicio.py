size = int(input("digite o tamanho do vetor:"))

vetor = []

for i in range(0,size,1):
    number = int(input("number:"))
    vetor.append(number) #insere o input nas posições do vetor
                         #no caso depois da ultima posicao inserida.
                         #posicao:0 , posicao:1, posicao:2 , ...

print(vetor)



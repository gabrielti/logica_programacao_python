
count = 0
vetor = [0,0,0,0,0]

while count < 5:
    numero = int(input("digite um numero par:"))

    if numero % 2 == 0:
        vetor[count] = numero
        count += 1

    else:
        while(numero % 2 != 0):
            numero = int(input("digite um numero PAR:"))
        
        vetor[count] = numero
        count +=1

for i in range(0,5,1):
    print(vetor[i])



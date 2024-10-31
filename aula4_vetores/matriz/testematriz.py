#essa parte que o a.append e matriz.append(a) faz no outro codigo
#-----------------------------------------------------------------
a = [0,1]
b = [2,3]

matriz = [a,b]
#-----------------------------------------------------------------

print(matriz)

for i in range(2):
    for j in range(2):
        print(matriz[i][j],end='')
    print()

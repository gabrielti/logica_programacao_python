
N = int(input("digite um inteiro:"))
mult = 1

for i in range(N,0,-1):
    anterior = mult
    mult = mult*i

print(f"{N}! = {mult}")       
        

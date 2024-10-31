stringA = input("text:")
lst =[]

tamanho = len(stringA)

for letter in stringA:
    lst.append(letter)

stringB = ['_'] * tamanho

print(stringA)
print(stringB)

for i in range(0,tamanho):
    stringB[i] = stringA[i]

print(stringB)
print(lst)

if(lst == stringB):
    print("igual")

else:
    print("diferente")

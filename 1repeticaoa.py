x = 10
y = 30
soma = 0

while (soma < x*y or x < y):

    soma = y - x
    x += soma
    y -= soma    

print(x, y, soma)

nota1 = float(input('digite nota1'))
nota2 = float(input('digita nota2'))

media = (nota1+nota2)/2

if(media >= 7):
    print('aprovado')

elif(media < 7 and media >= 5):
    print('recuperacao')

else:
    print('reprovado')

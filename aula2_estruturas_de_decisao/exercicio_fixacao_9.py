#program_name: informar qual o maior e o menor numero
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, logical statements and conditionals

nota_1 = float(input("nota_1:"))
nota_2 = float(input("nota_2:"))
nota_3 = float(input("nota_3:"))

sum = nota_1+nota_2+nota_3

if(sum/3 >= 7):
    print("aprovado")

else:
    print("reprovado")
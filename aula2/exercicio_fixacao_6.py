#program_name: informar qual o maior e o menor numero
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, logical statements and conditionals

year = int(input("year:"))

rest1 = year%4
rest2 = year%400

if(rest1 == 0): #condicao unica, se for f pula pro proximo if porque n tem um else interligado a ele
    print("ano bissexto")

if(rest2 == 0): #condicao interligado com o else, se v entao pula o else, se f entao vai pro else
    print("ano_bissexto")

else:
    print("ano nao bissexto")



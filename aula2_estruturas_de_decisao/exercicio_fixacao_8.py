#program_name: informar qual o maior e o menor numero
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, logical statements and conditionals

number = float(input("digite um dividendo:"))
divisor = float(input("digita um divisor:"))

if(number%divisor == 0):
    print(number,"multiplo de",divisor)

else:
    print("nao multiplo")
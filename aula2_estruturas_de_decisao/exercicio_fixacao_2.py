#program_name: inform if a person typed an vowel or consonant
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, logical statements and conditionals

letter = input("type a letter:")
letter = letter.upper() #() significa que nao tem limite de dados de entrada? Acho que sim

if(letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' ):
    print("vowel")

else:
    print("consonant")

#No C teria que usar else if, aqui seria elif, porque em C so e possivel comparar duas variaveis por vez
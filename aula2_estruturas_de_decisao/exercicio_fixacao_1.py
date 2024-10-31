#program_name: inform if a person has the same name as you
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, relational operators and conditions statements

name = input("whats your name?:")

name = name.upper() #transform the string letters into upper letters, to not happen GabRIel
                    #and compare to gabriel, for example. Case sensitive, but same name

if(name == "GABRIEL"):
    print("same name")

else:
    print("not the same name")


#bem mais simples, em C ele teria que comparar posicao por posicao na string. Ou seja, char por char
#o python ja faz isso automatico, embora C seja mais rapido por ser compilado, ao invez de interpretado
    
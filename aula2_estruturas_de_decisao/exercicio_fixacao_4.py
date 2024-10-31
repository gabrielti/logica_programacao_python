#program_name: informar qual o maior e o menor numero
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, logical statements and conditionals

number1 = float(input("primeiro_numero:"))
number2 = float(input("segundo_numero"))

if(number1 > number2):
   print("maior_numero:",number1)

else:
    print("maior_numero:",number2)

#todo if pode ter um else correlacionado. lembrando que o python trabalha com identacao
#print(f"maior_numero {number1}")
#print("texto1",var1,"text2",var2)
    
#if,elif e else
#ex: if(number%3 == 0), elif(number%5)


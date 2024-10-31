#program_name: calculate the arithmetic_mean of 5 ages
#author: gabriel_takiguchi(sidewinder)
#data: 06/03/24
#version: 1.0
#content: simple variable types, algorithm thinking and calculations

age1 = int(input("person_age:"))
age2 = int(input("person_age:"))
age3 = int(input("person_age:"))
age4 = int(input("person_age:"))
age5 = int(input("person_age:"))

#usar um loop, muita memoria desnecessaria alocada

arithmetic_mean = (age1+age2+age3+age4+age5)/5

print("age_arithmetic_mean:",arithmetic_mean) 
#outra sintaxe possivel: print(f"age_arithmetic_mean{arithmetic_mean}}"), concatenando
#como todos as idades sao inteiras, o resultado do valor/5, obrigatoriamente vai ser um inteiro. Se nao
#for, ele vai pegar somente a parte inteira? Nao, ele transforma em um float com 1 casa decimal...
#interessante
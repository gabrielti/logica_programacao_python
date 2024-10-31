#use python3 on terminal + file_directory path
#aparentemente todos os dados de input do python sao sempre strings, portanto e necessario converter str para int
#a identacao ( ) equivale a {} no C
#a principio o python automaticamente ja identifica o tipo de variavel, ex: se voce calcula com um int
#o resultado vai ser um int. tipos de dados
# 'a' char
# 'car' str
# classe, ponteiros 
# operadores aritmeticos
# operacoes aritmeticas (/ divisao normal , // divisao inteira)
# nomenclatura de variavies
# resolver problemas que ja resolvi + os que tem nos slides do canvas 

a = ord(input("number:"))
b = 8
c = "gabriel"
d = 'a'

if(a > b):
  print("ok")

else:
  print("not ok")

while(b > a):
  print(a)
  a = a+1

print(a,b,c,d)
print(type(c))
#program_name: informar o dia da semana com base em um numero
#author: gabriel_takiguchi(sidewinder)
#data: 13/03/24
#version: 1.0
#content: simple variable types, algorithm thinking, logical statements and conditionals

number = int(input("digite um numero entre 1 e 7:"))

if(number == 1):
    print("domingo")

if(number == 2):
    print("segunda")

if(number == 3):
    print("terca")

if(number == 4):
    print("quarta")

if(number == 5):
    print("quinta")

if(number == 6):
    print("sexta")

if(number == 7):
    print("sabado")

else:
    print("numero invalido")
    

#o else ocorre depois das verificacoes de todos os if's, nao e um bloco ligado com o ultimo if(number == 7)
#essa resolucao e feia, com certeza tem um metodo mais elegante
#lembrando que se usar so i if, se por exemplo eu tiver 3 if's, quando 1 desses if der positivo, ele vai
#pular todos os outros if's. ja com elif ele vai verificar os elif de baixo

#se for 1, vai pular o 2 if. se for elif ele vai verificar o if e mesmo que de verdadeiro, vai verificar o
#elif
    
#if(number == 1):
#   print("segunda")

#if(number == 2):
    #print("terca")
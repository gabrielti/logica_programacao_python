senha = input("crie_senha:")

top_cinco_senhas_mais_utilizadas = ['12345678','adminadmin','abcdefgh','senhasenha','password123']

n = 0

while(n<5):
    if senha == top_cinco_senhas_mais_utilizadas[n]:
        print("senha fraca")
    n = n+1 

#if, se V entao nao verifica o resto. Se F, verifica
#elif, se V entao nao verifica o resta. Se F, verifica. Incluindo outros elif
#else, caso todas as acima forem F, sera executada

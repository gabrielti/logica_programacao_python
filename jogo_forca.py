import time

palavra = ""
letras_usuario = []
chances = 0
ganhou = False

print("Bem vindo ao jogo da forca!")
time.sleep(1.5)
chances = int(input("Escolha quantas tentativas para seu amigo: "))
time.sleep(1)
palavra = input("Escolha uma palavra para seu amigo tentar advinhar: ")
print(f"O")
print(f"  O")
print(f"     O")
print(f"        O")
print(f"      O")
print(f"    O")
print(f"  O")
print(f"O")
while True:
    for letra in palavra:
        letra_encontrada = False
        for letra_usuario in letras_usuario:
            if letra.lower() == letra_usuario:
                print(letra, end=" ")
                letra_encontrada = True
                break
        if not letra_encontrada:
            print("_", end=" ")

    print(f"Você tem {chances} tentativas restantes!")
    tentativa = input("Escolha uma letra para advinhar: ")
    letras_usuario.append(tentativa.lower())

    letra_correta = False
    for letra in palavra:
        for letra_usuario in letras_usuario:
            if letra.lower() == letra_usuario:
                letra_correta = True
                break
        if not letra_correta:
            break

    if not letra_correta:
        chances -= 1

    ganhou = all(letra.lower() in letras_usuario for letra in palavra)

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou em {chances} tentativas! A palavra era: {palavra}")
else:
    print(f"Você perdeu! Suas chances acabaram. A palavra era: {palavra}") 
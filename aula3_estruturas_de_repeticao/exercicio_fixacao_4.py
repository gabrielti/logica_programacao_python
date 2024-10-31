import random

number = random.randrange(1,100)
print(f"{number}\n")
guess = int(input("digite um numero inteiro:"))

if(guess == number):
    print("acertou!")

else:
    while(guess != number):
        guess = int(input("digite outro numero inteiro:"))
    print("acertou!")



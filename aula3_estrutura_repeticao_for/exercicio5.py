razao = float(input("informe a razao:"))
primeiro_termo = float(input("informe o primeiro termo da P.A:"))
termo = int(input("informe o n-esimo termo desejado:"))

anterior = primeiro_termo

for i in range (1,termo,1):
    proximo = anterior + razao
    anterior = proximo

print(proximo)

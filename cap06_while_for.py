i = 0
while i < 5:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

print("Fin del ciclo while")

frutas = ["manzana", "pera", "uva", "sandía", "mango"]
for fruta in frutas:
    if fruta == "uva":
        continue
    print(fruta)

fruta = "manzana"
for letra in fruta:
    print(letra)

numeros = [0, 4, 5, 1, 3]
for numero in numeros:
    print(numero)

for x in range(5, 15, 2):
    print(x)

for i, fruta in enumerate(frutas):
    print(i, fruta)

frutas = ["manzana", "pera", "uva", "sandía", "mango"]
sabores = ["fea", "rica"]
for fruta in frutas:
    for sabor in sabores:
        print(fruta, sabor)

for i, fruta in enumerate(frutas):
    frutas[i] = fruta.replace("a", "o")

frutas

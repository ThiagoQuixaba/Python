#Média:
numero = [1, 0, 0, 0, 0]
soma = 0
while numero[0] < 5:
    numero[numero[0]] = float(input(f"Digite {numero[0]}° número: "))
    numero[0] = numero[0] + 1
numero[0] = 1
while numero[0] < 5:
    soma = soma + numero[numero[0]]
    numero[0] = numero[0] + 1
media = soma / 4
print(f"A média do numeros digitados é {media}")
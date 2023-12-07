#Code: Print e Input:
print("Digite o Valor 1:")
valor1 = input()
valor2 = input("Digite o Valor 2: ")

print(valor1)
print(valor2)
print("Os valores digitados foram", valor1, "e", valor2)
print("Os valores digitados foram {} e {}".format(valor1, valor2))
print("Os valores digitados foram %s e %s" % (valor1, valor2))
print(f"Os valores digitados foram {valor1} e {valor2}")

print ("Digite a primeira Nota")
nota1 = float(input())
print("Digite a segunda Nota")
nota2 = float(input())
media = (nota1 + nota2) / 2
print("A média é:", media)
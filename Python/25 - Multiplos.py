#Multiplos:
numeros = [float(input("Digite valor de A: ")), float(input("Digite valor de B: "))]
if numeros[0] % numeros[1] == 0 or numeros[1] % numeros[0] == 0:
    print("São múltiplos!")
else:
    print("Não são múltiplos!")
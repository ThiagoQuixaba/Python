#Série de fibonacci (for):
antecessores = [0, 1]
n = int(input("Insira valor de N: "))
for timer in range (1, n + 1):
    numero = antecessores[0] + antecessores[1]
    print(numero)
    antecessores[1] = antecessores[0]
    antecessores[0] = numero
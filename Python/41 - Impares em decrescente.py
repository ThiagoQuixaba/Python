#Impares em decrescente:
vetor = [0, int(input("Inserir valor inicial: ")), int(input("Inserir valor final: "))]
while vetor[1] > vetor[2]:
    vetor[2] = int(input("Inserir valor final: "))
for vetor[0] in range (vetor[2], vetor[1] - 1, -1):
    if vetor[0] % 2 != 0:
        print(vetor[0])
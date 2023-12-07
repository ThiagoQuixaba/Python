#Vetor em ordem crescente:
vetor = [3, 4, 1, 2]

for i in range(0, 4):
    for j in range(0, 3):
        if vetor[j] > vetor[j + 1]:
            aux = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = aux
        print(vetor)
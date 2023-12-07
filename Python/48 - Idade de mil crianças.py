#Idade de mil crianças:
vetoriadade = []
soma = 0
for i in range (0, 1000):
    vetoriadade.append(int(input(f"Digite a idade da {i + 1}° criança: ")))
    while vetoriadade[i] < 0:
        vetoriadade[i] = (int(input(f"Digite a idade da {i + 1}° criança: ")))
    soma += vetoriadade[i]

media = soma/vetoriadade.__len__()

for i in range(0, vetoriadade.__len__()):
    print(f"idade da {i + 1}° criança: {vetoriadade[i]}")

print(f"Média etária das crianças é de: {media}")
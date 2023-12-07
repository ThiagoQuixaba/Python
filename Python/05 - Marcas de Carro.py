#Marcas de carro
nomes = ["", "", ""]
i = 0
while i < 3:
    nomes[i] = str(input(f"Inserir {i + 1}° marca de carro: "))
    i = i + 1
i = 0
print("")
while i < 3:
    print(f"Marca{i + 1}: {nomes[i]}")
    i = i + 1
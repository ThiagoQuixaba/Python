#Cardapio:
i = 0
quantidade = 0
total = 0
preços = [3.00, 2.50, 2.50, 1.00, 3.00]
nomes = ["Hambúrguer", "Cheeseburger", "Fritas", "Refrigerante", "Milkshake"]

while i < 5:
    print(nomes[i], "............... R$:", preços[i])
    i = i + 1
i = 0
print("")
while i < 5:
    if i == 2:
        quantidade = int(input(f"Quantidade de porções de {nomes[i]}: "))
    else:
        quantidade = int(input(f"Quantidade de {nomes[i]}: "))
    total = total + (preços[i] * quantidade)
    i = i + 1
print(f"O total é R$:{total}")
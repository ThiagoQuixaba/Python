#Custo:
lucro = 0.12
roubo = 0.45
custo_inicial = float(input("Insira custo de fabrica: "))
custo_final = custo_inicial * (lucro + roubo + 1)
print("O custo do carro será de R$:", custo_final)
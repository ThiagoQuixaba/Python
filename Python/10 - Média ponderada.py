#Média ponderada.
notas = [1, 0, 0, 0]
pesos = [0, 0, 0]
nome = str(input("Inserir nome do aluno: "))

while notas[0] < 4:
    while True:
        notas[notas[0]] = float(input(f"Inserir {notas[0]}° nota de {nome}: "))
        if notas[notas[0]] >= 0 and notas[notas[0]] <= 10:
            pesos[notas[0] - 1] = float(input(f"Inserir peso da {notas[0]}° nota de {nome}: "))
            break
        else:
            print("Nota invalida! \n")
        pass
    notas[0] = notas[0] + 1

notas[0] = 1
soma_notas = 0
soma_pesos = 0

while notas[0] < 4:
    soma_notas = soma_notas + (notas[notas[0]] * pesos[notas[0] - 1])
    soma_pesos = soma_pesos + pesos[notas[0] - 1]
    notas[0] = notas[0] + 1

media_ponderada = soma_notas / soma_pesos
print(f"A média ponderada de {nome} é de {media_ponderada}")
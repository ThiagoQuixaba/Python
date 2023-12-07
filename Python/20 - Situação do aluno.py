#Situação do aluno:
nome = str(input("Digite nome do(a) aluno(a): "))
notas = [1, -1, -1]
pesos = [0, 0]
while notas[0] <= 2:
    while notas[notas[0]] < 0 or notas[notas[0]] > 10:
        notas[notas[0]] = float(input(f"Digite a {notas[0]}° nota de {nome}: "))
        if notas[notas[0]] < 0 or notas[notas[0]] > 10:
            print("Nota invalida! Tente novamente.")
    pesos[notas[0] - 1] = int(input(f"Digite o peso da {notas[0]}° nota de {nome}: "))
    notas[0] = notas[0] + 1
soma_notas = 0
soma_pesos = 0
notas[0] = 1
while notas[0] <= 2:
    soma_notas = soma_notas + (notas[notas[0]] * pesos[notas[0] - 1])
    soma_pesos = soma_pesos + pesos[notas[0] - 1]
    notas[0] = notas[0] + 1
media_ponderada = soma_notas / soma_pesos
if media_ponderada >= 6:
    situacao = "aprovado(a)"
elif media_ponderada >= 4:  
    situacao = "de recuperação"
else:
    situacao = "reprovado(a)"
print(f"A média de {nome} foi {media_ponderada} e ele está {situacao}.")
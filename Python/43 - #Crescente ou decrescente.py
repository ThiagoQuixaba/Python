#Crescente ou decrescente:
while True:
    escolha = str(input("C = crescente e D = decrescente: "))
    if escolha == "C" or escolha == "c":
        inicio = 0
        final = 21
        passo = 1
        break
    elif escolha == "D" or escolha == "d":
        inicio = 20
        final = -1
        passo = -1
        break
    else:
        pass
for timer in range (inicio, final, passo):
    print(timer)
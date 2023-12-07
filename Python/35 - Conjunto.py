#Conjunto:
contagem = 0
maior = 0
menor = 0
soma = 0
produto = 1
while True:
    opcao = str(input("Deseja adicionar um número ao conjunto?: "))
    while opcao != "s" and opcao != "S" and opcao != "sim" and opcao != "Sim" and opcao != "n" and opcao != "N" and opcao != "não" and opcao != "nao" and opcao != "Não" and opcao != "Nao":
        print("3RR0R! \nOpção invalida!")
        opcao = str(input("Deseja adicionar um número ao conjunto?: "))
    if opcao == "s" or opcao == "S" or opcao == "sim" or opcao == "Sim":
        valor = float(input("Digite um número: "))
        contagem += 1
        if contagem == 1:
            maior = valor
            menor = valor
            soma += valor
            produto *= valor
        else:
            if valor >= maior:
                maior = valor
            elif valor <= menor:
                menor = valor
            soma += valor
            produto *= valor
    else:
        break
print(f"O maior número digitado foi {maior}. \nO menor número digitado foi {menor}. \nA soma dos números digitados foi {soma}. \nO produto dos números digitados foi {produto}.")
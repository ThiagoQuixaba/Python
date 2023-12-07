#Converter dinheiro:
taxa_de_cambio = 0.203252033
while True:
    x = int(input("Você deseja comverter real para dóllar ou dóllar para real? (1 - real -> dóllar / 2 - dóllar -> real): "))
    if x == 1:
        real = float(input("Inserir valor em real: "))
        dollar = real * taxa_de_cambio
        print(f"O valor referente a R$:{real} em dóllares é de U$:{dollar}")
        break
    elif x == 2:
        dollar = float(input("Inserir valor em dóllar: "))
        real = dollar / taxa_de_cambio
        print(f"O valor referente a U$:{dollar} em reais é de R$:{real}")
        break
    else:
        print("Opção invalida! \n")
        pass
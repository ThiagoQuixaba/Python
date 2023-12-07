#Salário com comissão:
while True:
    nome = str(input("Digite nome do vendedor: "))
    valor_fixo = 1500.00
    quantidade = -1
    while quantidade < 0:
        quantidade = int(input(f"Digite a quantidade de carros vendidos por {nome}: "))
        if quantidade < 0:
            print("Não tem como vender uma quantidade negativa de carros!")
    comissão1 = 50.00 * quantidade
    if quantidade >= 1:
        valor_total_das_vendas = int(input(f"Digite O valor total vendido por {nome}: "))
        if valor_total_das_vendas < 0:
            print(f"Essa divida será descontada do salário de {nome}")
    else:
        valor_total_das_vendas = 0
    if valor_total_das_vendas >= 0:
        comissão2 = 0.05 * valor_total_das_vendas
        salario = valor_fixo + comissão1 + comissão2
        print(f"O salário total de {nome} é de R$:{salario}")
    else:
        comissão2 = valor_total_das_vendas
        salario = valor_fixo + comissão2
        if salario > 0:
            print(f"O salário total de {nome} é de R$:{salario}")
        elif salario == 0:
            print(f"{nome} não recebera salário")
        else:
            print(f"{nome} deve R$:{salario * -1} ")

    x = ""
    while x != "s" and x != "S" and x != "n" and x != "N":
        x = str(input("Deseja recomeçar? [S/N]: "))
        if x != "s" and x != "S" and x != "n" and x != "N":
            print ("ERR0R!")
    if x == "s" or x == "S":
        pass
    elif x == "n" or x == "N":
        break
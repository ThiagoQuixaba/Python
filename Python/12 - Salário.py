#Salário:
nome = str(input("Inserir nome do funcionário: "))
while True:
    salario_atual = float(input("Inserir salário atual: "))
    if salario_atual > 0:
        break
    elif salario_atual == 0:
        print("Salário invalido! Ele não é um funcionario, mas sim de um escravo! \nTente novamente.")
        pass
    else:
        print("Salário invalido! Isso não é um salario, mas sim uma divida! \nTente novamente.")
        pass

aumento_percentual = float(input("Inserir percentual de aumento ou de corte: "))
aumento_percentual = aumento_percentual / 100

if aumento_percentual >= 0:
    salario_final = salario_atual * (1 + aumento_percentual)
    print(f"O salário de {nome} depois do aumento será de R$:{salario_final}.")
else:
    salario_final = salario_atual * (1 - aumento_percentual)
    print(f"O salário de {nome} depois do corte será de R$:{salario_final}.")
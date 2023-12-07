#INSS:
while True:
    salario = float(input("Inserir valor do salário: "))
    if salario >= 0:
        break
    else:
        pass
if salario < 200:
    roubo = 0.08
elif salario < 500:
    roubo = 0.085
elif salario < 1000:
    roubo = 0.09
else:
    roubo = 0.095
desconto = salario * roubo
print(f"O valor do roub... quero dizer, desconto do INSS é de R$:{desconto}, o que equivale a {roubo}")
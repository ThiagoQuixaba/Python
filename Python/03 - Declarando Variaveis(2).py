#Code: Declarando variaveis:

#1° - Tirar a média de 4 numeros:
numero1 = float(input("Digite 1° numero: "))
numero2 = float(input("Digite 2° numero: "))
numero3 = float(input("Digite 3° numero: "))
numero4 = float(input("Digite 4° numero: "))
media = float((numero1 + numero2 + numero3 + numero4) / 4)

#2° - Calcular área do triângulo: 
altura = float(input("Digite altura: "))
comprimento = float(input("Digite comprimento: "))
area = float((altura * comprimento) / 2)

#3° - Converter um valor em R$ (real) para U$ (dollar):
real = float(input("Digite o valor em reais: "))
dolar = float(real / 5)

#4° - Converter a temperatura de °C (célsius) para °F(Fahrenheit);:
fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
celsius = float((fahrenheit - 32) / 1.8)

#5° - Aumentaro salário de um funcionário em 35%:
salario_atual = float(input("Digite o salário atual: "))
aumento = 0.35
salario_final = salario_atual * (1 + aumento)
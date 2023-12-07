#Área triângulo:
base = float(input("Inserir comprimento da base do triângulo: "))
while base < 0:
    base = float(input("Comprimento de base invalida! Inserir a largura do triângulo: "))
altura = float(input("Inserir a altura do triângulo: "))
while altura < 0:
    altura = float(input("Altura invalida! Inserir a altura do triângulo: "))
area = base * altura / 2
print(f"A área do triangulo é de {area}")
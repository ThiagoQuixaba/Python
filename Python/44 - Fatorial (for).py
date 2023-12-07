#Fatorial (for):
valor = int(input("Inserir Valor: "))
if valor >= 0:
    if valor == 0 or valor == 1:
        Resultado = 1
    if valor >= 2:
        resultado = valor
        for timer in range (valor -1, 1, -1):
            resultado *= timer
    print(f"{valor}! = {resultado}")
else:
    print(f"{valor}! não existe.")
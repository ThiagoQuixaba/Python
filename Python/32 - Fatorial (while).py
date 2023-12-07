#Fatorial (while):
Valor = int(input("Inserir Valor: "))
if Valor >= 0:
    if Valor == 0 or Valor == 1:
        Resultado = 1
    timer = Valor
    if timer >= 2:
        Resultado = Valor
        while timer > 2:
            Resultado = Resultado * (timer - 1)
            timer = timer - 1
    print(f"{Valor}! = {Resultado}")
else:
    print(f"{Valor}! não existe.")
#Série de fibonacci (while):
antecessores = [0, 1]
timer = 1
while timer <= 15:
    numero = antecessores[0] + antecessores[1]
    print(numero)
    antecessores[1] = antecessores[0]
    antecessores[0] = numero
    timer += 1
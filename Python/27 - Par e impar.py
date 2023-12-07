#par e Impar:
par = 0
impar = 0
while True:
    numero = float(input("Digite um número: "))
    if numero == -1:
        break
    elif numero % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"A quantidade de números pares digitada foi {par} e a quantidade de números impares digitados foi {impar}.")
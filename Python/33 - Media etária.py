#Media etária:
soma_etaria = 0
quantidade_de_pessoas = 0
while True:
    idade = int(input("Digite idade: "))
    if idade == 0:
        break
    else:
        soma_etaria += idade
        quantidade_de_pessoas += 1
        pass
media_etaria = soma_etaria / quantidade_de_pessoas
print(f"A media etaria desse conjunto de pessoas é de {media_etaria} anos.")
#Converter temperatura:
while True:
    x = int(input("Você deseja converter temperaturade de fahrenheit para célsius ou de célsius para fahrenheit? (1 - fahrenheit -> célsius / 2 - célsius -> fahrenheit): "))
    if x == 1:
        f = float(input("Inserir temperatura em fahrenheit: "))
        c = (f - 32) / 1.8
        print(f"A temperatura em célsius correspondente a {f} °F é {c} °C")
        break
    elif x == 2:
        c = float(input("Inserir temperatura em célsius: "))
        f = (c * 1.8) + 32
        print(f"A temperatura em fahrenheit correspondente a {c} °C é {f} °F")
        break
    else:
        print("Opção invalida! \n")
        pass
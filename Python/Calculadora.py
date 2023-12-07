while True:
    def Soma(valor1, valor2):
        resultado = valor1 + valor2
        return resultado
    
    def Subtracao(valor1, valor2):
        resultado = valor1 - valor2
        return resultado
    
    def Multiplicacao(valor1, valor2):
        resultado = valor1 * valor2
        return resultado
    
    def divisao(valor1, valor2):
        resultado = valor1 / valor2
        return resultado
    
    def percentual(valor1, valor2):
        valor1 = valor1 / 100 
        resultado = valor1 * valor2
        return resultado
    
    def fatorial(valor1):
        if valor1 == 0 or valor1 == 1:
            resultado = 1
            return resultado
        else:
            i = valor1
            if i >= 2:
                resultado = valor1
                while i > 2:
                    resultado = resultado * (i - 1)
                    i -= 1
                return resultado
    
    def potencia(valor1, valor2):
        resultado = valor1 ** valor2
        return resultado
    
    def raiz(valor1, valor2):
        resultado = valor1 ** (1 / valor2)
        return resultado
    
    def primo(valor1):
        i = 1
        y = 0
        while i < valor1 + 1:
            z = valor1 % i
            if z == 0:
                y += 1
            i += 1
        return y

    print("(Operações: Adição (+), Subtração (-), Multiplicação (*), Divisão (/), Fatorial (!), Potencia (p), Raiz (r), Primo (?), ...)")
    Operacao = str(input("Inserir Operação: "))

    if Operacao == "+":
        valor1 = float(input("Inserir Primeiro Valor: "))
        valor2 = float(input("Inserir Segundo valor: "))
        Resultado = Soma(valor1, valor2)
        print("A resultado é: ", resultado)

    if Operacao == "-":
        valor1 = float(input("Inserir Primeiro Valor: "))
        valor2 = float(input("Inserir Segundo valor: "))
        resultado = Subtracao(valor1, valor2)
        print(f"O resultado é {resultado}")
        
    if Operacao == "*":
        valor1 = float(input("Inserir Multiplicador: "))
        valor2 = float(input("Inserir Multiplicando: "))
        resultado = Multiplicacao(valor1, valor2)
        print(f"O resultado é {resultado}")

    if Operacao == "/":
        Valor1 = float(input("Inserir Dividendo: "))
        Valor2 = float(input("Inserir Divisor: "))
        if valor2 == 0:
            print("O resultado é Indefinido")
        else:
            resultado = divisao(valor1, valor2)
            print(f"O resultado é resultado")
    if Operacao == "%":
        valor1 = float(input("Inserir Valor Inicial: "))
        valor2 = float(input("Inserir Porcentagem: "))
        resultado = percentual(valor1, valor2)
        print(f"O resultado é {resultado}")
    if Operacao == "!":
        valor1 = float(input("Inserir Valor: "))
        if(valor1 == round(valor1)):
            if valor1 >= 0:
                resultado = fatorial(valor1)
                print(f"{valor1}! = {resultado}")
            else:
                print(F"{valor1}! não existe")
        else:
            print(F"{valor1}! não existe")
    if Operacao == "p":
        valor1 = float(input("Inserir Base: "))
        valor2 = float(input("Inserir Expoente: "))
        resultado = potencia(valor1, valor2)
        print(f"{valor1} elevado a {valor2} é igual a {resultado}")
    if Operacao == "r":
        valor1 = float(input("Inserir Radicando: "))
        valor2 = float(input("Inserir Índice: "))
        if valor2 == 0 or valor1 < 0:
            print(f"A raiz {valor2}° de {valor1} não existe no conjunto dos numeros reais!")
        else:
            resultado = raiz(valor1, valor2)
            print(f"A raiz {valor2}° de {valor1} é igual a {resultado}")
    if Operacao == "?":
        valor1 = float(input("Inserir Valor: "))
        if(valor1 == round(valor1)):
            y = primo(valor1)
            if y == 2:
                print(f"{valor1} é um numero primo!")
            else:
                print(f"{valor1} não é um numero primo!")
        else:
            print("O valor precisa ser inteiro!")   

    x = ""
    while x != "s" and x != "S" and x != "n" and x != "N":
        x = str(input("Deseja recomeçar? [S/N]: "))
        if x != "s" and x != "S" and x != "n" and x != "N":
            print ("ERR0R!")
    if x == "s" or x == "S":
        pass
    elif x == "n" or x == "N":
        break
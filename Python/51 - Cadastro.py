#Cadastro:
contagem = 0
nomes = []
CPFs = []
telefones = []
enderecos = []
opcao = [0, 0, 0, 0, 0]
while True:
    while True:
        print("[1 - Cadastrar / 2 - Editar / 3 - Listar / 4 - Em breve / 0 - Sair]")
        try:
            opcao[0] = int(input("Qual ação deseja fazer? "))
            if opcao[0] != 1 and opcao[0] != 2 and opcao[0] != 3 and opcao[0] != 4 and opcao[0] != 0:
                print("Ação Invalida! \n")
                pass
            else:
                break
        except:
            print("3RR0R! Tente Novamente. \n")
    if opcao[0] == 0:
        print("Finalizando Programa...")
        break
    elif opcao[0] == 1:
        while True:
            print("[1 - Novo cadastro / 0 - Voltar para menu]")
            while True:
                try:
                    opcao[1] = int(input("Qual ação deseja realizar?: "))
                    if opcao[1] != 1 and opcao[1] != 0:
                        print("Ação Invalida! Tente Novamente. \n")
                        pass
                    else:
                        break
                except:
                    print("3RR0R! Tente Novamente. \n")
            if opcao[1] == 1:
                try:
                    nomes.append(str(input("Insira Nome: ")))
                except:
                    print("3RR0R! \n")
                try:
                    CPFs.append(int(input("Insira CPF: ")))
                except:
                    print("3RR0R! \n")
                try:
                    telefones.append(int(input("Insira Telefones: ")))
                except:
                    print("3RR0R! \n")
                try:
                    enderecos.append(str(input("Insira Endereços: ")))
                except:
                    print("3RR0R! \n")
                contagem += 1
            else:
                break
    elif opcao[0] == 2:
        if contagem == 0:
            print("Nada foi cadastrado!")
        else:
            for i in range(0, contagem):
                print(f"{i + 1} - {nomes[i]}.")
            while True:
                try:
                    opcao[2] = int(input("Qual espaço deseja editar?: "))
                    if opcao[2] > contagem or opcao[2] < 1:
                        print("Esse espaço não existe! \n")
                        pass
                    else:
                        opcao[2] -= 1
                        break
                except:
                    print("Esse espaço não existe! \n")
            while True:
                print(f"1 - {nomes[opcao[2]]}. \n2 - {CPFs[opcao[2]]}. \n3 - {telefones[opcao[2]]}. \n4 - {enderecos[opcao[2]]} \n0 - Voltar.")
                while True:
                    try:
                        opcao[3] = int(input("Qual informação deseja editar?: "))
                        if opcao[3] < 0 or opcao[3] > 4:
                            print("Essa informação não existe! \n")
                            pass
                        else:
                            break
                    except:
                        print("Essa informação não existe! \n")
                if opcao[3] == 0:
                    break
                elif opcao[3] == 1:
                    nomes[opcao[2]] = str(input("Insira Novo Nome: "))
                elif opcao[3] == 2:
                    CPFs[opcao[2]] = int(input("Insira Novo CPF: "))
                elif opcao[3] == 3:
                    telefones[opcao[2]] = int(input("Insira Novo Telefone: "))
                elif opcao[3] == 4:
                    enderecos[opcao[2]] = str(input("Insira Novo Endereço: "))
    elif opcao[0] == 3:
        if contagem == 0:
            print("Nada foi cadastrado!")
        else:
            for i in range(0, contagem):
                print(f"{i + 1} - {nomes[i]}.")
            while True:
                try:
                    opcao[4] = int(input("Qual espaço deseja vizualizar as informações?: "))
                    if opcao[4] > contagem or opcao[4] < 1:
                        print("Esse espaço não existe! \n")
                        pass
                    else:
                        opcao[4] -= 1
                        break
                except:
                    print("Esse espaço não existe! \n")
            print(f"{nomes[opcao[4]]}. \n{CPFs[opcao[4]]}. \n{telefones[opcao[4]]}. \n{enderecos[opcao[4]]}.")
    elif opcao[0] == 4:
        print("Essa ação ainda não foi implementada. Pedimos perdão pelo transtorno.")
print("Programa Finalizado.")
senha_valida = "1234"
senha_digitada = input(print('Digite sua senha: '))
while True:
    if(senha_digitada == senha_valida):
        print('Acesso autorizado')
        break
    print('Senha Invalida!')
    senha_digitada = input(print('digite a senha correta'))
print('Continuação da aplicação')
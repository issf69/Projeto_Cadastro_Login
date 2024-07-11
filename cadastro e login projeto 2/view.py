from controller import ControllerCadastro, ControllerLogin



while True:
    print("=======[menu]==========")
    decidir = int(input('Digite 1 para cadastrar\nDigite 2 para logar\nDigite 3 para sair\n'))


    if decidir ==1:
        nome = input('Digie seu nome')
        email = input('Digie seu email')
        senha = input('Digie sua senha')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)


        if resultado == 2:
            print("Tamanho do nome digitado inválido")
        elif resultado == 3:
            print("Email maior que 200 caracteres")
        elif resultado == 4:
            print("Tamanho de senha inválido")
        elif resultado == 5:
            print("Email já cadastrado")
        elif resultado == 6:
            print("Erro interno")
        elif resultado == 1:
            print("Cadastro realizado com sucesso")
    elif decidir == 2:
        email = input('Digite seu email')
        senha = input('Digite sua senha')
        resultado = ControllerLogin.login(email, senha)
        if not resultado:
            print('Email ou senha invalido')
        else:
            print(resultado)
    else:
        break


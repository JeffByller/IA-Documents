usuario = []
ocorrencias = []
elogios = []
sugestoes = []
CPFS = []
def cadastro():
    while True:
        print('Forneça as informações do usuário!')

        dados = {}
        dados['nomecompleto'] = input('Nome:')
        dados['senha'] = input('Senha:')
        dados['cpf'] = int(input('CPF:'))

        dados['email'] = input('E-mail:')
        lista = {i['email']: i for i in usuario}
        while dados['email'] in lista:
            dados['email'] = input('E-mail em uso, tente novamente! \n E-mail:')

        dados['login'] = input('Digite o seu nome de usuário:')
        lista = {i['login']: i for i in usuario}
        while dados['login'] in lista:
            dados['login'] = input('Usuário em uso, tente outro usuário! \n Usuário:')

        dados['cpf'] = int(input('Repita o seu CPF:'))
        lista = {i['cpf']: i for i in usuario}
        while dados['cpf'] in lista:
            dados['cpf'] = int(input('CPF inválido ou em uso, digite novamente! \n CPF:'))


        usuario.append(dados)
        CPFS.append(dados['cpf'])
        print('CADASTRO CONCLUIDO!')
        break

def cadocor():
    while True:
        print('Por favor, faça o login!')
        lista = {i['login']: i for i in usuario}
        usu = input('Login: ')

        if usu in lista:
            print('Por favor, cadastre a sua ocorrência!')
            ocorrencia = {}
            ocorrencia['id'] = usu
            ocorrencia['ocorrencia'] = input('Digite a sua ocorrência:')
            ocorrencias.append(ocorrencia)
            print("Você poderia avaliar a nossa ouvidoria?")
            fdbk = int(input("Se sim, digite 1 Se não digite 2\n"))
            if fdbk == 1:
                input("Deixe aqui o seu feedback!\n")
                print("Obrigado por usar nossa ouvidoria!")
            elif fdbk > 2:
                print("Opção invalida!")
            elif fdbk == 2:
                break
            else:
                print("Obrigado por usar nossa ouvidoria!")
        else:
            print('Usuário não encontrado!')

def cadelogio():
    while True:
        print("Por favor, faça o login!")
        lista = {i['login']: i for i in usuario}
        usu = input('Login:')
        if usu in lista:
            print("Por favor, cadastre o seu elogio!")
            elogio = {}
            elogio['id'] = usu
            elogio['elogio'] = input('Digite o seu elogio')
            elogios.append(elogio)
            print("Você poderia avaliar a nossa ouvidoria?")
            fdbk = int(input("Se sim, digite 1 Se não digite 2\n"))
            if fdbk == 1:
                input("Deixe aqui o seu feedback!\n")
                print("Obrigado por usar nossa ouvidoria!")
            elif fdbk > 2:
                print("Opção invalida!")
            elif fdbk == 2:
                break
            else:
                print("Obrigado por usar nossa ouvidoria!")
                break

        else:
            print('Usuário não encontrado!')

def cadsugest():
    while True:
        print("Por favor, faça o login!")
        lista = {i['login']: i for i in usuario}
        usu = input('Login:')
        if usu in lista:
            print("Por favor, cadastre a sua sugestão!")
            sugestao = {}
            sugestao['id'] = usu
            sugestao['sugestão'] = input('Digite a sua sugestão')
            sugestoes.append(sugestao)
            print("Você poderia avaliar a nossa ouvidoria?")
            fdbk = int(input("Se sim, digite 1 Se não digite 2\n"))
            if fdbk == 1:
                input("Deixe aqui o seu feedback!\n")
                print("Obrigado por usar nossa ouvidoria!")
            elif fdbk > 2:
                print("Opção invalida!")
            elif fdbk == 2:
                break
            else:
                print("Obrigado por usar nossa ouvidoria!")
        else:
            print('Usuário não encontrado!')

def mostrardados1():
    while True:
        print("Forneça o login para consultar as ocorrências registradas.")

        lista = {i['login']: i for i in usuario}
        usu = input('Login:')

        if usu in lista:
            print("Aqui está o resultado da sua pesquisa:")
            result = list(filter(lambda item: item['id'] == usu,ocorrencias))
            for i in result:
                print(i)

        else:
            print("Usuário não encontrado.")

        alt = input("Deseja verificar outro dado? (S/N):").strip().lower()
        if (alt =='n'):
            break

def mostrardados2():
    while True:
        print("Forneça o login para consultar as ocorrências registradas.")

        lista = {i['login']: i for i in usuario}
        lista2 = {i['id']: i for i in CPFS}
        usu = input('Login:')

        if usu in lista and usu not in lista2:
            print(f'Dados do usuário [{usu.upper()}]: {lista[usu]}')

            print("CPF não cadastrado!")

        elif usu in lista and usu in lista2:
            print(f'Dados do usuário [{usu.upper}]: {lista[usu]}')
            print(f'CPF do usuário [{usu.upper()}:')
            result = list(filter(lambda item: item['id'] == usu,elogios))
            for i in result:
                print(i)

        else:
            print("Usuário não encontrado.")

        alt = input("Deseja verificar outro dado? (S/N):").strip().lower()
        if (alt =='n'):
            break

def mostrardados3():
    while True:
        print("Forneça o login para consultar as ocorrências registradas.")

        lista = {i['login']: i for i in usuario}
        usu = input('Login:')

        if usu in lista:
            print(f'Dados do usuário [{usu.upper()}]: {lista[usu]}')

            print("CPF não cadastrado!")

        elif usu in lista:
            print(f'Dados do usuário [{usu.upper}]: {lista[usu]}')
            print(f'CPF do usuário [{usu.upper()}:')
            result = list(filter(lambda item: item['id'] == usu,sugestoes))
            for i in result:
                print(i)

        else:
            print("Usuário não encontrado.")

        alt = input("Deseja verificar outro dado? (S/N):").strip().lower()
        if (alt =='n'):
            break

def apagardados():
    while True:
        print("Por favor, faça o login!")
        lista = {i['login']: i for i in usuario}
        usu = input('Login:')
        if usu in lista:
            alt1 = input("Deseja apagar todos os seus dados? (S=1/N=2)")
            if alt1 == 1:
                ocorrencias.clear()
                print("Você apagou todos os dados cadastrados.")
                break
        else:
            print("Nenhum dado foi apagado")
            break

def menu():
    print("-"*60)
    print("(1) Cadastrar-se na ouvidoria")
    print("(2) Cadastrar ocorrência")
    print("(3) Cadastrar elogio")
    print("(4) Cadastrar sugestão")
    print("(5) Listar ocorrências")
    print("(6) Listar elogios")
    print("(7) Listar sugestões")
    print("(8) Apagar dados")
    print("-"*60)

menu()

while True:
    opc = int(input("Escolha -> (1) (2) (3) (4) (5) (6) (7) (8)\n"))
    while opc > 9 or opc < 0:
        print("Opção invalida, por favor digite novamente!")

    if opc == 1:
        cadastro()
    elif opc == 2:
        cadocor()
    elif opc == 3:
        cadelogio()
    elif opc == 4:
        cadsugest()
    elif opc == 5:
        mostrardados1()
    elif opc == 6:
        mostrardados2()
    elif opc ==7:
        mostrardados3()
    elif opc ==8:
        apagardados()
    else:
        print("Opção invalida, encenrrando ouvidoria...")
        break


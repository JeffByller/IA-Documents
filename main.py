usuarios = []
ocorrencias = []
elogios = []
sugestoes = []
# ----------------------------
# Funções de Usuário
# ----------------------------
def cadastro():
    print("\n=== Cadastro de Usuário ===")
    dados = {}

    dados["nome"] = input("Nome completo: ").strip()
    dados["senha"] = input("Senha: ").strip()

    # Validação de CPF
    while True:
        try:
            cpf = input("CPF (somente números): ").strip()
            if not cpf.isdigit():
                raise ValueError
            if any(u["cpf"] == cpf for u in usuarios):
                print("CPF já cadastrado!")
            else:
                dados["cpf"] = cpf
                break
        except ValueError:
            print("CPF inválido!")

    # Validação de e-mail
    while True:
        email = input("E-mail: ").strip().lower()
        if any(u["email"] == email for u in usuarios):
            print("E-mail já em uso!")
        else:
            dados["email"] = email
            break

    # Validação de login
    while True:
        login = input("Usuário (login): ").strip()
        if any(u["login"] == login for u in usuarios):
            print("Login já em uso!")
        else:
            dados["login"] = login
            break

    usuarios.append(dados)
    print("Cadastro realizado com sucesso!")

def login_usuario():
    """Solicita login e retorna o usuário se existir"""
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            return u
    print("Usuário ou senha incorretos!")
    return None

# ----------------------------
# Funções de Cadastro de Dados
# ----------------------------
def registrar(tipo, lista):
    user = login_usuario()
    if not user:
        return

    print(f"\nDigite sua {tipo}:")
    texto = input("> ").strip()
    registro = {"usuario": user["login"], tipo: texto}
    lista.append(registro)
    print(f"{tipo.capitalize()} registrada com sucesso!")

    # Feedback opcional
    opc = input("Gostaria de avaliar o sistema? (S/N): ").strip().lower()
    if opc == "s":
        fb = input("Deixe seu feedback: ")
        print("Obrigado pela contribuição!")

# ----------------------------
# Funções de Listagem
# ----------------------------
def listar(lista, tipo):
    user = login_usuario()
    if not user:
        return

    print(f"\n=== Seus(as) {tipo}s ===")
    encontrados = [i for i in lista if i["usuario"] == user["login"]]

    if encontrados:
        for i, item in enumerate(encontrados, start=1):
            print(f"{i}. {item[tipo]}")
    else:
        print(f"Nenhum(a) {tipo} registrado(a).")

# ----------------------------
# Função de exclusão
# ----------------------------
def apagar_dados():
    user = login_usuario()
    if not user:
        return

    confirma = input("Deseja realmente apagar todos os seus dados? (S/N): ").strip().lower()
    if confirma == "s":
        global usuarios, ocorrencias, elogios, sugestoes
        usuarios = [u for u in usuarios if u["login"] != user["login"]]
        ocorrencias = [o for o in ocorrencias if o["usuario"] != user["login"]]
        elogios = [e for e in elogios if e["usuario"] != user["login"]]
        sugestoes = [s for s in sugestoes if s["usuario"] != user["login"]]
        print("Todos os dados foram apagados!")
    else:
        print("Operação cancelada.")

# ----------------------------
# Menu Principal
# ----------------------------
def menu():
    while True:
        print("\n" + "-"*40)
        print(" OUVIDORIA ".center(40, "-"))
        print("1 - Cadastrar usuário")
        print("2 - Registrar ocorrência")
        print("3 - Registrar elogio")
        print("4 - Registrar sugestão")
        print("5 - Listar ocorrências")
        print("6 - Listar elogios")
        print("7 - Listar sugestões")
        print("8 - Apagar dados")
        print("0 - Sair")
        print("-"*40)

        try:
            opc = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida!")
            continue

        if opc == 1: cadastro()
        elif opc == 2: registrar("ocorrência", ocorrencias)
        elif opc == 3: registrar("elogio", elogios)
        elif opc == 4: registrar("sugestão", sugestoes)
        elif opc == 5: listar(ocorrencias, "ocorrência")
        elif opc == 6: listar(elogios, "elogio")
        elif opc == 7: listar(sugestoes, "sugestão")
        elif opc == 8: apagar_dados()
        elif opc == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# ----------------------------
# Início do Programa
# ----------------------------
menu()


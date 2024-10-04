# Variáveis globais
LIMITE_SAQUES = 3
usuarios = []  # Lista para armazenar os usuários
contas = []    # Lista para armazenar as contas
numero_conta = 1  # Inicia o número da conta em 1

# Função para realizar um saque (recebe argumentos por nome)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

# Função para realizar um depósito (recebe argumentos por posição)
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Função para exibir o extrato (argumentos posicionais e nomeados)
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    cpf = input("Informe o CPF (apenas números): ")
    usuario_existente = filtrar_usuario(cpf)

    if usuario_existente:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

# Função para filtrar um usuário pelo CPF
def filtrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar uma nova conta corrente vinculada a um usuário
def criar_conta_corrente():
    global numero_conta
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        numero_conta += 1
        print(f"Conta número {conta['numero_conta']} criada com sucesso para o usuário {usuario['nome']}!")
    else:
        print("Usuário não encontrado, cadastre o usuário antes de criar a conta.")

# Menu principal
def menu_principal():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [cu] Cadastrar Usuário
    [cc] Criar Conta Corrente
    [q] Sair
    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "cu":
            cadastrar_usuario()

        elif opcao == "cc":
            criar_conta_corrente()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Inicializa o programa
if __name__ == "__main__":
    menu_principal()

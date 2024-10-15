class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Por favor, informe um valor positivo.")

    def saque(self, valor):
        if self.saques_diarios < 3 and valor <= 500:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_diarios += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente. Não é possível realizar o saque.")
        else:
            print("Limite de saques diários excedido ou valor de saque inválido.")

    def extrato(self):
        print("Extrato da conta:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

banco = Banco()

while True:
    print("\nOpções:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        banco.deposito(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        banco.saque(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

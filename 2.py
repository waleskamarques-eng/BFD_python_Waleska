#Questão 2 Sistema bancário

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def exibir_informacoes(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"

# Classe filha que herda da classe Cliente
class ContaCorrente(Cliente):
    def __init__(self, nome, cpf, endereco, saldo=0.0):
        # Chama o construtor da classe pai
        super().__init__(nome, cpf, endereco)
        self.saldo = saldo

# Método para depósito
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido para depósito.")

# Método para saque
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido.")

# Método específico da classe filha
    def verificar_saldo(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print("Endereço atualizado com sucesso.")

# Teste
conta = ContaCorrente("Maria Souza", "987.654.321-00", "Av. das Américas, 1200", 500)

# Chamadas de métodos
print(conta.exibir_informacoes())
print(conta.verificar_saldo())

conta.depositar(200)
conta.sacar(100)
conta.sacar(1000)# tentativa inválida, maior que o saldo

print(conta.verificar_saldo())

conta.alterar_endereco("Rua das Flores, 300")
print(conta.exibir_informacoes())

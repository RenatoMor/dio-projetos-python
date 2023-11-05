from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

# Cliente -----------------------------------------------
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Pessoa Física -----------------------------------------
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Conta -------------------------------------------------
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente para realizar o saque.")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!\n\nRetire as notas da máquina.")
            self.historico.adicionar_transacao(Saque(valor, self))

        else:
            print("Informe um valor válido para saque.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nInsira as notas na máquina para realizar o depósito.\n\nDepósito efetuado com sucesso!")
            self.historico.adicionar_transacao(Deposito(valor, self))
        else:
            print("\nInforme um valor válido para depósito.")

# Conta Corrente ----------------------------------------
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = 0
        for transacao in self.historico.transacoes:
            if transacao["tipo"] == "Saque":
                numero_saques += 1

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nExcedeu o limite de saque!\n\nPor favor, informe um valor menor.")

        elif excedeu_saques:
            print("\nExcedeu o número limite de saques!\n\nPor favor, tente novamente mais tarde.")

        else:
            super().sacar(valor)

    def __str__(self):        
        return f"""\
        ================= Dados da Conta ===================
            \tAgência:\t\t{self.agencia}
            \tC/C:\t\t\t{self.numero}
            \tTitular:\t\t{self.cliente.nome}
            \tSaldo:\t\t\tR$ {self.saldo:.2f}
            \tLimite:\t\t\tR$ {self._limite:.2f}
            \tLimite Saques:\t\t{self._limite_saques}
        ====================================================
        """
        
# Histórico ----------------------------------------------
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m%Y %H:%M:%S"),
                "saldo": transacao.conta.saldo,
            }
        )

# Transação ----------------------------------------------
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Saque -------------------------------------------------
class Saque(Transacao):
    def __init__(self, valor, conta):
        self._valor = valor
        self._conta = conta

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    @property
    def conta(self):
        return self._conta

# Depósito ----------------------------------------------
class Deposito(Transacao):
    def __init__(self, valor, conta):
        self._valor = valor
        self._conta = conta

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    @property
    def conta(self):
        return self._conta

# Cores para o Terminal ---------------------------------
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
AZUL = "\033[96m"
ENDC = "\033[0m"

# Menu --------------------------------------------------
def menu():
    menu_text = """
{red}================ MENU ================{end}
   {green}\t[d]\t\tDepositar{end}
    {green}\t[s]\t\tSacar{end}
    {green}\t[e]\t\tExtrato{end}
    {green}\t[nc]\t\tNova conta{end}
    {green}\t[lc]\t\tListar contas{end}
    {green}\t[nu]\t\tNovo usuário{end}
    {green}\t[q]\t\tSair{end}
{red}======================================{end}

=> """.format(azul=AZUL, blue=BLUE, red=RED, green=GREEN, end=ENDC)
    
    return input(textwrap.dedent(menu_text))

# Filtrar Cliente ---------------------------------------
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Recuperar Conta Cliente -------------------------------
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nNão há contas cadastradas nesse CPF!")
        return

    return cliente.contas[0]

# Depositar ---------------------------------------------
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nNão há cliente cadastrado com esse CPF!")
        return

    try:
        valor = float(input("\nInforme o valor do depósito: R$ "))
        transacao = Deposito(valor, None)

        conta = recuperar_conta_cliente(cliente)
        if not conta:
            return

        transacao = Deposito(valor, conta)
        cliente.realizar_transacao(conta, transacao)
    except ValueError:
        print("\nValor inválido. Tente novamente!")

# Sacar -------------------------------------------------
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nNão há cliente cadastrado com esse CPF!")
        return

    try:
        valor = float(input("\nInforme o valor do saque: R$ "))
        transacao = Saque(valor, None)

        conta = recuperar_conta_cliente(cliente)
        if not conta:
            return

        transacao = Saque(valor, conta)
        cliente.realizar_transacao(conta, transacao)
    except ValueError:
        print("\nValor inválido. Tente novamente!")

# Exibir Extrato ----------------------------------------
def exibir_extrato(clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nNão há cliente cadastrado com esse CPF!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n============================= EXTRATO =============================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não há transações para exibir!"
    else:
        for transacao in transacoes:
            tipo = transacao['tipo']
            valor = f"R$ {transacao['valor']:.2f}"
            data = transacao['data']
            extrato += f"\n{tipo:<10}\t{valor:<15} - \tData: {data}"


    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("===================================================================")

# Criar Cliente ------------------------------------------
def criar_cliente(clientes):
    cpf = input("Por favor, insira o CPF do cliente 'apenas números': ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n Já existe um cliente registrado com esse CPF em nosso sistema.")
        return
    print('\nDados Pessoais:-------------------------------------------------------------------')
    nome = input("\nNome completo: ")
    data_nascimento = input("Data de nascimento - dd/mm/aaaa: ")
     
    print('\nEndereço Completo:----------------------------------------------------------------')
    endereco = input("\nEndereço completo - [logradouro, número - bairro - cidade/UF]:\n")
    print('------------------------------------------------------------------------------------')
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\nAgradecemos por escolher nossos serviços.\nSeu cadastro foi concluído com êxito!")

# Criar Conta --------------------------------------------
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nNão foi possível encontrar o cliente com os dados fornecidos!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nParabéns! Sua conta foi criada com sucesso!\n\nEstamos animados em tê-lo(a) como nosso cliente.\nAgora você tem acesso a todos os recursos e \nbenefícios disponíveis em nossa plataforma.")

# Listar Contas ------------------------------------------
def listar_contas(contas):
    for conta in contas:        
        print(textwrap.dedent(str(conta)))

# Main --------------------------------------------------
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nOps! Parece que ocorreu uma operação inválida.\nPor favor, selecione novamente a operação desejada. ")


if __name__ == "__main__":
    main()

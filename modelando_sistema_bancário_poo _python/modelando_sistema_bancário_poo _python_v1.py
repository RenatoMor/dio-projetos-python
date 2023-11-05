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


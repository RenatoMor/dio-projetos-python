import datetime
# cores para o terminal-------------------------------------
RED = "\033[91m"
BLUE = "\033[94m"
ENDC = "\033[0m"
# menu------------------------------------------------------
menu = """
==================== MENU ====================
[1] {blue}Depositar{end}
[2] {red}Sacar{end}
[3] Extrato
[0] Sair
==============================================

=> """.format(blue=BLUE, red=RED, end=ENDC)
# variáveis-------------------------------------------------
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
# loop principal---------------------------------------------   
while True:
    opcao = input(menu)
# depósito--------------------------------------------------
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            data_transacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            transacao = {"data": data_transacao, "descricao": "Depósito", "valor": valor}
            extrato.append(transacao)
        else:
            print("Operação falhou! O valor informado é inválido.")
# saque-----------------------------------------------------
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou! Excedeu o limite diario de saque.")
        elif valor > 0:
            saldo -= valor
            data_transacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            transacao = {"data": data_transacao, "descricao": "Saque", "valor": valor}
            extrato.append(transacao)
            numero_saques += 1
        else:
            print("O valor informado é inválido! Tente novamente.")
# extrato---------------------------------------------------
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in extrato:
                data = transacao["data"]
                descricao = transacao["descricao"]
                valor = transacao["valor"]
                if descricao == "Depósito":
                    cor_descricao = BLUE
                elif descricao == "Saque":
                    cor_descricao = RED
                else:
                    cor_descricao = ENDC
                print(f"{data} - {cor_descricao}{descricao}{ENDC}: R$ {valor:.2f}")
        print(f"\nSaldo: {BLUE}R$ {saldo:.2f}{ENDC}")
        print("==========================================")
# sair------------------------------------------------------
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

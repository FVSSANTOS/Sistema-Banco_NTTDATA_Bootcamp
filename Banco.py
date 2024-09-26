import textwrap

def menu ():    
    menu = """\n
        ============= MENU =============
        [D] \tDepositar
        [S] \tSacar
        [NU] \tNovo usuário
        [NC] \tNova conta
        [LC] \tListar contas
        [E] \tExtrato
        [Q] \tSair
==> """
    return input(textwrap.dedent(menu))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao.upper() == 'D':
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato) 
        
        elif opcao.upper() == "S":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao.upper() == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.upper() == "NU":
            criar_usuario(usuarios)
        
        elif opcao.upper() == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_saques, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao.upper() == "LC":
            listar_contas(contas)
        
        elif opcao.upper() == "Q":
            break
        
        else:
            print("Opção inválida !!!")


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Você não tem saldo suficiente.")
    elif valor > limite:
        print("Você o ultrapassou o valor limite de saque.")
    elif numero_saques >= limite_saques:
        print("Você ultrapassou o limite de saques diários.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor: .2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Valor informado inválido. @@@")
    
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ====== EXTRATO ======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("========================")
def criar_usuario(usuarios):
    pass

def criar_conta():
    pass

def listar_contas():
    pass





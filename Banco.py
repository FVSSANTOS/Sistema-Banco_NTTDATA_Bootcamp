menu = """

[D] Depositar
[S] Saque
[E] Extrato
[Q] Sair


==> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3



while True:

    opcao = input(menu)

    if opcao.upper() == 'D':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R${valor: .2f}\n"
        else:
            print("Valor inválido!")
    
    elif opcao.upper() == "S":
        valor = float(input("Informe o valor do saque: "))

        if valor <= saldo and valor <= 500 and numero_saque <= LIMITE_SAQUES and valor > 0:
            saldo-=valor
            extrato += f"Saque de R${valor: .2f}\n"
            numero_saque+=1
        
        elif valor > saldo:
            print("Você não tem saldo suficiente.")

        elif valor > 500:
            print("Você ultrapassou o valor limite de saque.") 

        elif valor > LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários.")      
        
        elif valor < 0:
            print("Operação inválida.")

    elif opcao.upper() == "E":

        print("\n=====Extrato=====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================")
    
    elif opcao.upper() == "Q":
        break

    else:
        print("Operação inválida.")

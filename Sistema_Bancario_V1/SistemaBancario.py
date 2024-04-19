menu = """
    Menu

[1]-Depositar

[2]- Sacar

[3]- Extrarto

[4]- Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valDepo= float(input("Informe o valor de deposito: R$ "))

        if valDepo > 0:
            saldo += valDepo
            extrato += f"Deposito: R$ {valDepo}\n"
        else:
            print("Falha na opração! Valor invalido")

    
    elif opcao == "2":
        valSaque = float(input("Informe o valor de Saque: R$ "))

        excedeu_saldo= valSaque > saldo
        excedeu_limite = valSaque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de saque.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valSaque > 0:
            saldo = saldo - valSaque
            extrato += f"Saque: R$ {valSaque:.2f}\n"
            numero_saques += 1


        else:
            print("Operação falhou! O valor informado é inválido.")
            print("Falha na opração! Valor invalido")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    
    elif opcao == "4":
       break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

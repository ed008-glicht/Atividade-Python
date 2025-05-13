opcao= 0
while opcao !=5:
    print("Cardápio")
    print("1 - Hamburguer")
    print("2 - Pizza")
    print("3 - Salada")
    print("4 - Refrigerante")
    print("5 - Sair")
    opcao= int(input("Escolha uma opção: "))
    if opcao==1:
        print("Você escolheu Hamburguer")
    elif opcao==2:
        print("Você escolheu Pizza")
    elif opcao==3:
        print("Você escolheu Salada")
    elif opcao==4:
        print("Você escolheu Refrigerante")
    elif opcao==5:
        print("Saindo do cardápio")
        break
    else:
        print("Opção invalida, tente novamente.")
print("----------Calculadora simples---------")
opcao= 0
while opcao!=5:
    print("-----Calculadora-----")
    print ("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao= int(input("Digite sua opção: "))
    if opcao>=1 and opcao<=4:
        numero1= float(input("Informe o primeiro número: "))
        numero2= float(input("Informe o segundo número: "))
    if opcao== 1:
        resultado= numero1+numero2
        print(f"O Resultado da sua soma é {resultado:.0f}")
    elif opcao== 2:
        resultado= numero1-numero2
        print(f"O Resultado da sua subtração é {resultado:.0f}")
    elif opcao==3:
        resultado= numero1*numero2
        print(f"O Resultado da sua multiplicação é {resultado:.0f}")
    elif opcao== 4:
        resultado= numero1/numero2
        print(f"O Resultado da sua subtração é {resultado:.1f}")
    elif opcao== 5:
        print("saindo da calculadora, obrigado pela preferencia!")
        print("-------------------------------------------------")
        break
    else:
        print("Opção incorreta, tente novamente.")
valorFrances=0
valorIntegral=0
valordoceLiso=0
valordoceFarofa=0
valorForma=0
valorTotal=0
pao_doce_farofa=0
fraces=0
integra=0
pao_forma=0
doce_liso=0
opcao = 1
while opcao !=6:
    print ("\n----BEM-VINDO A NOSSA PADARIA----\n")
    print ("[1] Pão Francês")
    print ("[2] Pão Integral")
    print ("[3] Pão Doce liso")
    print ("[4] Pão Doce Farofa")
    print ("[5] Pão de Forma")
    print ("[6] Fim da compra")
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        fraces = float(input("Informe a quantidade desejada: ")) 
        valorFrances = fraces* 1.04
    elif opcao == 2:
        integra = float(input("Informe a quantidade desejada: "))
        valorIntegral = integra*1.04
    elif opcao == 3:
        doce_liso = float(input("Informe a quantidade desejada: "))
        valordoceLiso = doce_liso*1.08
    elif opcao == 4:
        pao_doce_farofa = float(input("Informe a quantidade desejada: "))
        valordoceFarofa = pao_doce_farofa*1.11
    elif opcao == 5:
        pao_forma = float(input("Informe a quantidade desejada: "))
        valorForma = pao_forma*0.95
    elif opcao == 6:
        print("\nResumo da compra: \n")
        if fraces >0:
            print (f"Pão francês - Quantidade: {fraces:.0f} | Valor: R$: {valorFrances:.2f}")
        if integra >0:
            print (f"Pão integral - Quantidade: {integra:.0f} | Valor: R$: {valorIntegral:.2f}")
        if doce_liso >0:
            print (f"Pão doce liso - Quantidade: {doce_liso:.0f} | Valor: R$: {valordoceLiso:.2f}")    
        if pao_doce_farofa >0:
            print (f"Pão doce farofa - Quantidade: {pao_doce_farofa:.0f} | Valor: R$: {valordoceFarofa:.2f}")
        if pao_forma >0:
            print (f"Pão de forma - Quantidade: {pao_forma:.0f} | Valor: R$: {valorForma:.2f}")
            break
    else:
        print ("Opção invalida, tente novamente")    
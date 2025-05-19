opcao=0
while opcao!=3:
    print("------Conversor de temperatura------")
    print("Escolha 1 para conversão de celsius para fahrenheit")
    print("Escolha 2 para conversão de celcius para kelvin")
    print("---------------------------------------------------")
    opcao= int(input("Escolha uma opção: "))
    temperatura_inicial = float(input("Informe a temperatura: "))
    if opcao==1:
        temp_final=(temperatura_inicial*9/5)+32
        print(f"A temperatura em Fahrenheint é {temp_final}")
    elif opcao==2:
        temp_final=temperatura_inicial/273.15
        print(f"A temperatura em Kelvin é {temp_final}")
    else:
        print("Saindo do conversor de Temperatura")
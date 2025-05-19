input("Escreva seu nome: ")
salario_fixo= float(input("Nos informe seu salário: "))
total_vendas= int(input("Quantas vendas você fez? "))
#Entrada de informações
comissao= salario_fixo*0.15
salario_final= salario_fixo+comissao
#Declaração de outras variaveis
if (total_vendas>=20):
    print("----Parabéns----")
    print("Você atingiu a meta!")
    print(f"Sua comissão será de {comissao}")
    print(f"O valor final do seu salário é de R$ {salario_final}")
else:
    print("----Que pena----")
    print("Você não atingiu a meta.")
    print(f"Seu salário final é de R$ {salario_fixo}")
input("Digite seu nome: ")
peso= float(input("Digite seu peso: "))
altura= float(input("Digite sua altura: "))
print("----------------------")
imc= peso/(altura*altura)
print(f"Seu IMC é de {imc:.1f}")

if imc<18.5:
    print("Abaixo do peso.")
elif imc>=18.5 and imc<=24.9:
    print("Peso normal.")
elif imc>=25.0 and imc<=29.9:
    print("Sobrepeso.")
else:
    print("Obeso.")
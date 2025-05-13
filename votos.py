ano_atual= 2025
ano_nascimento= int(input("Digite seu Ano de Nascimento: "))
idade= ano_atual-ano_nascimento
print(f"Você tem {idade} anos.")
if idade<16:
    print("Você não pode votar!")
elif idade<18 or idade>70:
    print("Seu voto é opcional.")
elif idade>=18 and idade<70:
    print("Seu voto é obrigatorio!")
#Declarar variáveis
import random
numero_secreto = random.randint(1,10)
tentativas=0 
contagem_tentativas = 0
#Introdução ao jogo 
print("Bem-vindo ao jogo do Número Secreto.")
print("Tente adivinhar o número secreto")
#Laço de repetição 
while tentativas != numero_secreto:
    numero = int(input("Digite um número:"))
    contagem_tentativas=contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns!Você adivinhou o número ")
        print(f"você precisou de {contagem_tentativas} tentativas.")
        break
    elif numero <numero_secreto:
        print("o número secreto é maior.")
    else:
        print("O número secreto é menor.")


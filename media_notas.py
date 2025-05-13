numero1= float(input("Digite sua primeira Nota: "))
numero2= float(input("Digite sua segunda Nota: "))
#Usuário coloca as indormações
media= (numero1+numero2)/2
#Calculo média
print(f"Sua média é {media}")
if media>=7:
    input("Você foi aprovado!")
else:
    input("Você foi reprovado :(")
#Reprovado ou Aprovado

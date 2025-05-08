import os
os.system("cls")


# nota1 = float (input("Digite a Primeira nota: "))
# nota2 = float (input("Digite a Segunda nota: "))

# media = (nota1 + nota2)/2
# print(f"Sua media é {media}")

# if media<5:
#     print("Reprovado")
# elif media >=5 or media >=6 or media ==7:
#     print("Em recuperação")
# elif media>7:
#     print("Aprovado")


#atividade IMC


# peso =float(input("Digite seu Peso: "))
# alt =float(input("Digite sua altura: "))
# imc = peso / (alt * alt)
# print (f"Seu IMC é: {imc:.2f} ")
# if imc < 17:
#     print("Situação: Muito abaixo do peso")
# elif imc>=17 and imc<=18.49:
#     print("Situação: Abaixo do peso")
# elif imc>=18.5 and imc<=24.99:
#     print("Situação: Peso normal")
# elif imc>=25 and imc<=29.99:
#     print("Situação: Acima do peso")
# elif imc>=30 and imc<=34.99:
#     print("Situação: Obesidade I")
# elif imc>=35 and imc<=39.99:
#     print("Situação: Obesidade II")
# elif imc>=40:
#     print("Situação: Obesidade III")


#ativadade autocar


print("-----TABELA DE SALARIOS-----")
print("Salarios até R$2799.99, aumento de 20%")
print("Salarios até R$2800.00, aumento de 15%")
print("Salarios até R$7000.00, aumento de 10%")
print("Salarios até R$15000.00, aumento de 5%")

salario  = float(input("Digite seu salario: "))
if salario<=2799.99:
    aumento = salario * 0.20
    total1 = aumento + salario
    print(f"Seu salario antes do reajuste: {salario} ")
    print("O percentual de aumento que sera aplicado é: 20% ")
    print(f"O seu salario com o aumento sera: {total1}")

elif salario<=2800:
    aumento2 = salario * 0.15
    total2 = aumento2 + salario
    print(f"Seu salario antes do reajuste: {salario} ")
    print("O percentual de aumento que sera aplicado é: 15% ")
    print(f"O seu salario com o aumento sera: {total2}")

elif salario<=7000:
    aumento3 = salario * 0.10
    total3 = aumento3 + salario
    print(f"Seu salario antes do reajuste: {salario} ")
    print("O percentual de aumento que sera aplicado é: 10% ")
    print(f"O seu salario com o aumento sera: {total3}")

elif salario<=15000:
    aumento4 = salario * 0.05
    total4 = aumento4 + salario
    print(f"Seu salario antes do reajuste: {salario} ")
    print("O percentual de aumento que sera aplicado é: 5% ")
    print(f"O seu salario com o aumento sera: {total4}")





import os
os.system("cls")

#Continuação input com Int e Float
#int() -> converte para inteiro
#float()-> converte para numero quebrado

# # #exemplo2
#  num1 = input("digite um numero: ")
#  soma = float(num1) + 15
#  print("a soma de" ,num1 , "+", "15" ,"=", soma)

# #exemplo3
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)

exemplo = float(input("digite o preco do produto: "))
desconto = 0.15 * exemplo
print("o preco do produto com 15% de desconto é ",exemplo-desconto)
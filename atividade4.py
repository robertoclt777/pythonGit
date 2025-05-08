import os
os.system("cls")

print("=======CAIXA=======")
produto1 = input("digite o produto:")
produto2 = input("digite o produto: ")
preco1 = float(input("Digite o preco do produto: "))
preco2 = float(input("Digite o preco do produto: "))
desconto= preco1 * 0.10
desconto2= preco2 * 0.25
print(f"O valor total do {produto1} será:", preco1 - desconto)
print(f"O valor total do {produto2} será:", preco2 - desconto2)
total =(preco1 - desconto + preco2 - desconto2)
print ("=======TOTAL=======")
print("Total R$", total)
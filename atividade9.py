import os 
os.system("cls")


# ("-------- LOJA DE APARELHOS ---------")

# print(r"""
# 1-Iphone 15 - R$5000,00
# 2-Xiaomi Redmi 13 pro plus 512 GB - R$2500,00
# 3-Sansung S25 265 GB - R$6999,99""")

# print(r"""
# FRETE:  SP -> 10,00
#          MG -> 15,00
#          rs -> 20,00""")
# n=float(input("Digite o numero do produto: "))
# s=input("Digite a sigla do estado: ").upper()
# print("-----------------------------")

# match n:
#     case 1:
#         preco=5000.00
#         print("Preço R$:5000,00")
#     case 2:
#         preco=2500.00
#         print("Preço R$2500,00")
#     case 3:
#         preco=6999.99
#         print("Preço R$6999,99")
# match s:
#     case "SP":
#         frete=10.00
#     case "MG":
#         frete=15.00
#     case "RS":
#         frete=20.00

# print(f"PREÇO R${preco}")
# print(f"FRETE R${frete}")
# print(f"TOTAL: R${preco + frete}")

import random

jogada=input("DIGITE PEDRA, PAPEL OU TESOURA: ")
papel= "papel"
pedra= "pedra"
tesoura="tesoura"

match jogada:
    case _ if jogada == papel:
        print(r"""PAPEL
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)   """)
    case _ if jogada == pedra:

        print(r""" PEDRA 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___))   """)
    case _ if jogada == tesoura:
        print(r""" TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)    """)



bot = 0
bot = random.randint(1,3)

match bot:
    case _ if bot == 1:
        print(r""" PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)   """)
        
    case _ if bot == 2:
        print(r""" PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    case _ if bot == 3:
        print(r""" TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)     """)
            
    















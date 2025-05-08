import random

jogada=input("DIGITE PEDRA, PAPEL OU TESOURA: ")
papel= "papel"
pedra= "pedra"
tesoura="tesoura"

match jogada:
    case _ if jogada == papel:
        print(r"""VOCÊ ESCOLHEU: PAPEL
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)   """)
    case _ if jogada == pedra:

        print(r"""VOCÊ ESCOLHEU: PEDRA 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___))   """)
    case _ if jogada == tesoura:
        print(r"""VOCÊ ESCOLHEU: TESOURA
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
        print(r"""A MAQUINA ESCOLHEU: PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)   """)
        
    case _ if bot == 2:
        print(r"""A MAQUINA ESCOLHEU: PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    case _ if bot == 3:
        print(r"""A MAQUINA ESCOLHEU: TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)     """)
        
result1= bot == 1 and jogada == pedra
result2= bot == 2 and jogada == pedra
result3= bot == 3 and jogada == pedra
result4= bot == 1 and jogada == papel
result5= bot == 2 and jogada == papel
result6= bot == 3 and jogada == papel
result7= bot == 1 and jogada == tesoura
result8= bot == 2 and jogada == tesoura
result9= bot == 3 and jogada == tesoura

if result1:
        print("VOCÊ PERDEU")
elif result2:
    print("EMPATOU")
elif result3:
    print("VOCÊ GANHOU!!!")
elif result4:
    print("EMPATOU")
elif result5:
    print("VOCÊ GANHOU!!!")
elif result6:
    print("VOCÊ PERDEU")
elif result7:
    print("VOCÊ GANHOU!!!")
elif result8:
    print("VOCÊ PERDEU")
elif result9:
    print("EMPATOU")
    



# 1=PAPEL 2=PEDRA 3=TESOURA
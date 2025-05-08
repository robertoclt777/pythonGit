import os
os.system("cls")

# linguagem = 100

# match linguagem:

#     case "python":
#         print("e facil")
#     case "java":
#         print("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case " js":
#         print("sou do back")
#     case "html":
#         print("kaua nao dorme")
#     case 10:
#         print("entrou aqui")
#     case _ :
#         print("outro caso")



print("Domingo-1")
print("Segunda-2")
print("Terça-3")
print("Quarta-4")
print("Quinta-5")
print("Sexta-6")
print("Sabado-7")

dsemana=float(input("Digite um dia da semana:"))

match dsemana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("an oruann")

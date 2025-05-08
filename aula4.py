import os
os.system("cls")

#upper() -> converter tudo para maiusculo
#lower() -> converter tudu para minusculo

letra= input("Digite uma Letra: ").lower

if letra =="a"or letra =="e"or letra =="i"or letra =="o"or letra =="u":
    print("Você digitou uma vogal!")
else:
    print("Você digitou uma consoante!")

#reescrevendo de outra maneira
#and or in

l = input("Digite uma letra")

if l in "aeiouAEIOU":
    print =("vogal")
else:
    print("consoante")


import os
os.system("cls")

quant = float (input("DIgite a quantidade de maças que deseja levar: "))
if quant >= 12:
    print(f"O valor a ser pago é R$ {quant *0.25}")
else:
    print(f"O valor a ser pago é R$ {quant *0.30}  ")
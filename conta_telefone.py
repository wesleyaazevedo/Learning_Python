"""Resolução de problema
Considere uma empresa de telefonia. Abaixo de 200 minutos a empresa cobra R$ 0,20
Entre 200 e 400 minutos, preço é R$ 0,18. Acima de 400 minutos o preço é R$ 0,18.
Calcule sua conta de telefone"""

#Problema retirado do Curso Python para Zumbis 

minutos = int(input("Informe quantos minutos foram utilizados: "))

if minutos < 200:
    conta = minutos * 0.20
    print('-'*43)
    print("Minutos: %5.2f\nVal/min:0.20"%minutos)
    print("Valor da conta: R$%5.2f" %conta)
elif minutos < 400:
    conta = minutos * 00.18
    print('-'*43)
    print("Minutos: %5.2f\nVal/min:0.18" %minutos)
    print("Valor da conta: R$%5.2f" %conta)
elif minutos >= 400:
    conta = minutos * 0.15
    print('-'*43)
    print("Minutos: %5.2f\nVal/min:0.15" %minutos)
    print("Valor da conta: R$%5.2f" %conta)

print('-'*20+'FIM'+'-'*20)


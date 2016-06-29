

vel = float(input("Digite a velocidade em que estava: "))
velp = 110
if vel > velp:
    multa = (vel - velp)*5
    print ('_'*50)
    print("Voce foi multado em: R$ %5.2f" %multa)
else:
    print ('_'*50)
    print("Parabéns! Você respeita as leis de trânsito.")

    

'''
    Programa para calcular quantidades de tintas
    necessárias para pintar uma determinada área.

    Considere que 1 litro de tinta pinta 3m² e que
    a tinta é vendida em latas de 18 litros, que
    custam R$ 80,00.
    Informe ao usuario a quantidade de tinta a serem
    compradas e o preço total.
    obs.: são vendidos apenas latas inteiras.
'''

metros = int(input("Digite quantos metros serão pintados: "))

while metros != 0:
#Utilizamos o resto da divisão, se diferente de 0 \
# precisaremos de mais uma lata

    if metros%54!= 0: 
    #Pegamos apenas a parte inteira da divsão
    #Adcionamos mais uma lata para a "rebarba"
        latas = int(metros/54) + 1

# Se o reto for 0 então apenas utilizamos o valor
# diretamente.
    else:
        latas = metros / 54

#valor = latas * 80 - Poderiamos definir o valor antes de imprimir
# ou calcular dentro do print, como fiz.
    print('-'*45)
    print("Voce vai precisar de: %d latas \nValor: R$%.2f" %(latas,latas*80))
    print('-'*45)
    
    metros = int(input("Digite quantos metros serão pintados: "))

print("\n")
print('-'*21+'FIM'+'-'*21)


    
    

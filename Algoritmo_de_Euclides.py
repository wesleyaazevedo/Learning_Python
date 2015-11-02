'''
    Dados dois números inteiros positivos, determinar o máximo divisor
    comum entre eles usando o algoritmo de Euclides.
    a   b   a%b
    21  15  6
    15  6   3
    6   3   0
'''
a = int(input('a: '))
b = int(input('b: '))

while a%b != 0:
    a, b = b, a%b
    print('\na: %d\nb: %d' %(a,b))

print('mdc = %d' %b)


#Código do curso Python para Zumbis

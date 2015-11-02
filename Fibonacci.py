

""" Função geradora da Sequência de Fibonacci"""
"""
Foi retirado do Tutorial de Python escrito
por Guido V.R.
"""

def fib(n): # Write Fibonacci series up to n
    a, b = 0,1
    while b < n:
        print (b)
        a, b = b, a+b

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

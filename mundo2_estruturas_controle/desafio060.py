""" DESAFIO 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
*CÁLCULO DE FATORIAL*
"""

""" 3 formas abaixo de como calcular o fatorial: """

#1 
# from math import factorial
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n,f))

#2

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

#3

# n = 10
# for i in range(n,1,-1):
#     print('{}'.format(i), end=' → ')
# print('FIM')





















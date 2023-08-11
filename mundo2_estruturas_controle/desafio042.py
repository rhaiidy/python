""" DESAFIO 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero = todos os lados iguais
- Isósceles = dois lados iguais
- Escaleno = todos os lados diferentes
*ANALISANDO TRIÂNGULOS v2.0*
"""

""" DESAFIO 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem 
ou não formar um triângulo.
*ANALISANDO TRIÂNGULOS v1.0*
"""
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas medidas é SIM possível formar um triângulo.')
    if r1 == r2 and r2 == r3 and r3 == r1: # r1 == r2 == r3
        print('Esse triângulo seria um triângulo EQUILÁTERO.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2: 
        print('Esse triângulo seria um triângulo ISÓSCELES.')
    elif r1 != r2 and r2 != r3 and r3 != r1: # r1 != r2 != r3 != r1
        print('Esse triângulo seria uma triângulo ESCALENO.')
else:
    print('Não é possível formar um triângulo.')

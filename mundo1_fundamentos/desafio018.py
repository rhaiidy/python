""" DESAFIO 018: Faça um programa que leia um ângulo qualquer e mostre na tela o o valor do seno,
cosseno e tangente desse ângulo. 
*SENO, COSSENO E TANGENTE*
"""
# import math

# angulo = int(input('Digite o ângulo: '))
# seno = math.sin(math.radians(angulo))
# cosseno = math.cos(math.radians(angulo))
# tangente = math.tan(math.radians(angulo))

# print ('SENO {:.2f}\nCOSSENO {:.2f}\nTANGENTE {:.2f}' .format(seno,cosseno,tangente))

from math import radians,sin,cos,tan

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('SENO {:.2f}\nCOSSENO {:.2f}\nTANGENTE {:.2f}' .format(seno,cosseno,tangente))


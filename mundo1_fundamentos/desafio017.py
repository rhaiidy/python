""" DESAFIO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
calcule e mostre o comprimento da hipotenusa. 
*CATETOS E HIPOTENUSA*
"""
# from math import sqrt

# cat_opo = float(input('Digite o comprimento do cateto oposto: '))
# cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
# #hipo = sqrt((cat_opo**2)+(cat_adj**2))
# #hipo = (cat_opo **2 + cat_adj**2) ** (1/2)
# print('O valor da hipotenusa é {:.2f}' .format(hipo))

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print ('O comprimento da hipotenusa é igual a {:.2f}' .format(hi))



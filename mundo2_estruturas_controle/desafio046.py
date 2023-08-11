""" DESAFIO 046: Faça um programa que mostre na tela uma contagem regressiva para os fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.

*CONTAGEM REGRESSIVA*
"""
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BOOM')
print('POOOW')
print('HAPPY NEW YEAR!!')

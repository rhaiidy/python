""" DESAFIO 051: Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. 
No final, mostre os 10 primeiros termos dessa progressão.
*PROGRESSÃO ARITMÉTICA*
"""

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = pt + (10-1)*razao #cálculo do décimo termo da PA. 10-1 pq ele quer os 10 primeiros números da PA

for i in range(pt,decimo_termo+razao,razao):
    print('{}'.format(i), end=' → ')
print('FIM')
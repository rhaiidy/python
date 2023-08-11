""" DESAFIO 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o 
maior e o menor peso lidos.
*MAIOR E MENOR DA SEQUÊNCIA*
"""
maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}kg.'.format(maior)) 
print('O menor peso lido foi de {:.1f}kg.'.format(menor)) 
    
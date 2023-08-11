""" DESAFIO 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
*VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO*
"""

cid = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

# quer saber se a palavra tem SANTO nas primeiras 5 letras
""" DESAFIO 053: Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços. 
*DETECTOR DE PALÍNDROMO*
ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

frase = str(input("Digite sua frase para saber se ela é ou não um palíndromo:  ")).strip().upper() #eliminou espaços externos
palavras = frase.split() # eliminou espaços internos e dividiu
junto = ''.join(palavras) # juntou
inverso = junto[::-1]
if inverso == junto:
    print('O inverso de {} é {}'.format(inverso,junto))
    print('A frase digitada É um palíndromo.')
else:
    print('Essa frase não é um palíndromo: {} {}'.format(junto,inverso))

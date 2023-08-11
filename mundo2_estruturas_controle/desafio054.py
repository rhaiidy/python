""" DESAFIO 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (21 anos)
*GRUPO DE MAIORIDADE*
"""
from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1,8):
    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        totmaior += 1 
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
print('E também {} menores de idade.' .format(totmenor))






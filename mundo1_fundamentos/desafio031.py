""" DESAFIO 031: Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem,
cobrando R$0.50 por KM para viagens de até 200km e R$0.45 para viagens mais longas.
*CUSTO DA VIAGEM*
"""

km = float(input('Digite a distância: '))
taxa_1 = km * 0.50
taxa_2 = km * 0.45

if km <=200:
    print('Como sua viagem será de {:.0f}km, sua passagem custará R${:.2f}'.format(km,taxa_2))
else:
    print('Sua viagem terá mais de 200km, então sua passagem custará R${:.2f}'.format(taxa_2))
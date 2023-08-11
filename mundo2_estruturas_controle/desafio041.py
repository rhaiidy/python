""" DESAFIO 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade: 
- Até 9 anos = mirim
- Até 14 anos = infantil 
- Até 19 anos = junior
- Até 25 anos = sênior
- Acima = master
*CLASSIFICANDO ATLETAS*
"""
from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - ano_nascimento

if idade <=9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <=25:
    print('SÊNIOR')
else:
    print('MASTER')
    
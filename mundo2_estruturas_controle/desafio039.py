""" DESAFIO 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
O programa também deverá mostrar o tempo que falta ou que passou do prazo.

*ALISTAMENTO MILITAR*
"""
from datetime import date 
ano_nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano_nasc
print('Quem nasceu em {} tem {} anos no ano de {}'.format(ano_nasc,idade,atual))

if idade < 18:
    tr = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para o seu alistamento.' .format(tr))
    ano = atual + tr
    print('Seu alistamento será em {}.'.format(ano))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade >18:
    tp = idade - 18
    print('Você já passou do tempo de alistamento a {} anos.'.format(tp))
    ano = atual - tp
    print('Seu alistamento foi em {}'.format(ano))


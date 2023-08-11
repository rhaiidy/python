""" DESAFIO 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da PA usando a estrutura WHILE.
*SUPER PROGRESSÃO ARITMÉTICA v2.0*
"""

""" DESAFIO 051: Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. 
No final, mostre os 10 primeiros termos dessa progressão.
*PROGRESSÃO ARITMÉTICA*
"""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
c = 1
while c <= 10:
    print('{} → '.format(termo), end=' ')
    termo += razao
    c += 1 



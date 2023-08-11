""" DESAFIO 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
*TRATANDO VÁRIOS VALORES v1.0*
"""

n = c = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    if n == 999:
        soma -= 999  
    c += 1
print('Você digitou um total de {} números e a soma entre eles é de {}.'.format(c,soma))
print('Fim do programa.')


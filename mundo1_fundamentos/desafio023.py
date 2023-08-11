""" DESAFIO 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados por unidade,
dezena, centena e milhar. 
*SEPARANDO DÍGITOS DE UM NÚMERO*
"""

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}' .format(num))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))




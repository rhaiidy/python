""" DESAFIO 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma msg:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.

*COMPARANDO NÚMEROS*
"""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O primeiro número ({}) é maior.'.format(n1))
elif n2 > n1:
    print('O segundo número ({}) é maior.'.format(n2))
else:
    print('{} e {} são iguais!'.format(n1,n2))

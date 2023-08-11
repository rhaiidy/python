""" DESAFIO 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
*JOGO DE ADIVINHAÇÃO v2.0*
"""

""" DESAFIO 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar advinhar qual foi o número escolhido pelo computador. O pc deverá escrever na tela
se o usuário venceu ou perdeu.

 *JOGO DE ADIVINHAÇÃO v1.0*
"""

from random import randint

num = int(input('Digite um número entre 0 e 10 e tente advinhar o número secreto: '))
escolhido = randint(0,10)
print(escolhido)
while num != escolhido:
    num = int(input('Ainda não foi dessa vez. Tente de novo! Digite outro número: '))
print('YES! Você acertou! Parabéns! O número era {}.'.format(escolhido))


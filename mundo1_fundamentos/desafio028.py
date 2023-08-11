""" DESAFIO 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar advinhar qual foi o número escolhido pelo computador. O pc deverá escrever na tela
se o usuário venceu ou perdeu.

 *JOGO DE ADIVINHAÇÃO v1.0*
"""

# import random
# import emoji

# num = int(input('Digite um número entre 0 e 5 e tente advinhar o número secreto: '))
# escolhido = random.randint(0,5)
# #print(escolhido)
# if num == escolhido:
#     print('Parabéns! Você acertou! 🥳👏')
# else:
#     print(emoji.emojize('Infelizmente não foi dessa vez.😕 Tente novamente.'))

from random import randint
from time import sleep
import emoji 

print('~'*51)
print('Vou escolher um número entre 0 e 5, tente advinhar!')
print('~'*51)

jogador = int(input('Qual número eu escolhi? '))
escolhido = randint(0,5) # número gerado aleatoriamente
print('WAAAAAIT FOR IT...')
sleep(2)

if jogador == escolhido:
    print('PARABÉNS!🥳 Tu é o brabo mesmo!👏')
else: 
    print(f'Não foi dessa vez, campeão.😕 O número que eu pensei foi {escolhido}.')


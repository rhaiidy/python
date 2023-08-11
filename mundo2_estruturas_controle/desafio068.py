""" DESAFIO 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
*JOGO DO PAR OU ÍMPAR*
"""
from random import randint
v = 0

while True:
    numero_usuario = int(input('Digite um número: '))
    numero_pc = randint(0,11)
    total = numero_usuario + numero_pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar? [P/I]  ")).strip().upper()[0]
    print(f'Você jogou {numero_usuario} e o PC jogou {numero_pc}. O total é {total}', end=' ► ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else: 
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
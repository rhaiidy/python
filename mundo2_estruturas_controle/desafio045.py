""" DESAFIO 045: Crie um programa que faça o computador jogar JOKENPÔ com você. 
*GAME PEDRA PAPEL TESOURA*
"""

import random

pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'

escolha_usuario = str(input('Vamos brincar? Pedra, Papel ou Tesoura? ')).upper()
jokenpo = ['PEDRA','PAPEL','TESOURA']
escolha_pc = random.choice(jokenpo)
print(escolha_pc)

if escolha_usuario == escolha_pc:
    print('Você escolheu {} e eu também escolhi {}.'.format(escolha_usuario,escolha_pc))
    print('Vamos jogar novamente!')
elif escolha_usuario == 'PEDRA' and escolha_pc == 'PAPEL':
    print('Você escolheu {}\n Eu escolhi {}\n PAPEL EMBRULHA PEDRA!\n VOCÊ PERDEU! PONTO PRA MIM! :)'.format(escolha_usuario,escolha_pc))
elif escolha_usuario == 'PEDRA' and escolha_pc == 'TESOURA':
    print('Você escolheu {}\n Eu escolhi {}\n PEDRA QUEBRA TESOURA!\n VOCÊ GANHOU! \o/'.format(escolha_usuario,escolha_pc))
elif escolha_usuario == 'PAPEL' and escolha_pc == 'TESOURA':
    print('Você escolheu {}\n Eu escolhi {}\n TESOURA CORTA PAPEL!\n VOCÊ PERDEU! PONTO PRA MIM! :)'.format(escolha_usuario,escolha_pc))
elif escolha_usuario == 'PAPEL' and escolha_pc == 'PEDRA':
    print('Você escolheu {}\n Eu escolhi {}\n PAPEL EMBRULHA PEDRA!\n VOCÊ GANHOU! \o/'.format(escolha_usuario,escolha_pc))    
elif escolha_usuario == 'TESOURA' and escolha_pc == 'PEDRA':
    print('Você escolheu {}\n Eu escolhi {}\n PEDRA QUEBRA TESOURA!\n VOCÊ PERDEU! PONTO PRA MIM! :)'.format(escolha_usuario,escolha_pc))
elif escolha_usuario == 'TESOURA' and escolha_pc == 'PAPEL':
    print('Você escolheu {}\n Eu escolhi {}\n TESOURA CORTA PAPEL!\n VOCÊ GANHOU! \o/'.format(escolha_usuario,escolha_pc))







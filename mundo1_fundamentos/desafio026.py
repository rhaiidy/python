""" DESAFIO 026: Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece por último 
*PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING*
"""

# 'A sociedade é apenas uma selva disfarçada.'
# 'Quem não tem bons filtros não sabe a água que bebe.'

frase = str(input('Digite uma frase: ')).upper().strip()
# Quantas vezes aparece a letra 'A'
print ('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
# Em que posição ela aparece pela primeira vez
print ('A letra "A" aparece pela primeira vez no indice {}'.format(frase.find('A')))
# Em que posição ela aparece por último 
print ('A letra "A" aparece pela última vez no indice {}'.format(frase.rfind('A')+1))

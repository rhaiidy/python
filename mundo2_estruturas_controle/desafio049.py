""" DESAFIO 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando o laço FOR.
*TABUADA v2.0*
"""

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n,c,n*c))


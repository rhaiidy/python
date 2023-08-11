""" DESAFIO 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
*CONTAGEM DE PARES*
"""
cont = 0
for c in range(2,51,2):
     if c % 2 ==0:
        cont += 1
        print(c, end=' ')
print('Existem {} números pares entre 1 e 50.'.format(cont))        

      
    
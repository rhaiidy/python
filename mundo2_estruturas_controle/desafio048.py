""" DESAFIO 048: Faça um programa que calcule a soma entre os números ímpares que são múltiplos de 3 e 
que se encontram no intervalo de 1 até 500.
*SOMA ÍMPARES MÚLTIPLOS DE 3*
"""
soma = 0
contador = 0
for c in range(1,501,2):
    if c % 3 ==0:
        contador += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}.'.format(contador,soma))
      
    


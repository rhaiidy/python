""" DESAFIO 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.
*SOMA DOS PARES*
"""
contador = 0
soma = 0
for c in range(1,7): 
    n = int(input('Digite o valor {}: '.format(c)))
    if n % 2 == 0:
        contador +=1
        soma += n
print('Os números pares digitados são: {}'.format(contador))
print('A soma entre eles é de {}'.format(soma))

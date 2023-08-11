""" DESAFIO 065: Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
*MAIOR E MENOR VALORES*
"""
c = soma = media = maior = menor = 0
continuar = 'S' 
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? S/N  ')).strip().upper()[0]
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / c
print('A média entre os números digitados é de {:.2f}'.format(media))
print('O menor valor digitado foi {} e o maior {}'.format(menor,maior))


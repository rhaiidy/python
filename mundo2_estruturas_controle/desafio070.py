""" DESAFIO 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar. No final, mostre:
a) qual total gasto na compra ok
b) quantos produtos custam mais de R$1000,00
c) qual é o nome do produto mais barato
*ESTATÍSTICAS EM PRODUTOS*
"""
tot = totmil = menor = c = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).upper()
    preco = float(input('Preço: R$'))
    c += 1
    tot += preco
    if preco >1000:
        totmil += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


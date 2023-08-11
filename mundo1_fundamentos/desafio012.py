""" Desafio 012: Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto."""

preco_original = float(input('Qual o preço do seu produto? R$'))
percentual = 5
desconto = (percentual*preco_original) / 100
#print(desconto)
preco_com_desconto = preco_original - desconto
#print(preco_com_desconto)
print(f'O seu produto de R${preco_original} está saindo por apenas R${preco_com_desconto}')


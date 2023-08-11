""" DESAFIO 015: Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.
*ALUGUEL DE CARROS*
"""

diarias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você rodou? '))
valor_diaria = diarias * 60
valor_km = km * 0.15
total_a_pagar = valor_diaria + valor_km 
print('O total a pagar é de R${:.2f}'.format(total_a_pagar))


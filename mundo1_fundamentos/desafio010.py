""" Desafio 010: Faça um programa que converta o valor de REAL para DÓLAR.
Considerar os valores: 
$1 = R$3,27 """

real_na_carteira = float(input('Quantos reais vc tem na carteira? R$'))
valor_em_dolar = (real_na_carteira / 3.27)
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real_na_carteira,valor_em_dolar))

"""Faça um programa que converta o valor de DÓLAR para REAL.
Considerar os valores: 
$1 = R$3,27 """

dolar = float(input('Quantos dólares você tem? '))
real = dolar *3.27
print(f'Você tem o equivalente a {real} reais.')
print(' ${:.2f} = R${:.2f}'.format(dolar,real), end=' ')
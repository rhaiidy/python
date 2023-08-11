""" DESAFIO 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não deve exceder 30% do salário ou então o empréstimo 
será negado.

*APROVANDO EMPRÉSTIMO*
"""

valor_emprestimo = float(input('Qual valor da casa que deseja financiar? R$'))
salario = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você pretende pagar esse empréstimo? '))
meses = anos*12
#print(meses)
salario_util = (salario*30)/100 # cálculo de 30% do salário
#print(salario_util)

valor_prestacao = valor_emprestimo / meses
#print(valor_prestacao)

if valor_prestacao >= salario_util:
    print('Para pagar R${:.2f} em {} anos, sua parcela seria de R${:.2f}, o que excederia "30%" do seu salário.'.format(valor_emprestimo,anos,valor_prestacao))
    print('Seu empréstimo foi NEGADO!.')
else:
    print('Seu empréstimo foi aprovado com sucesso!')
    print('Você pagará o empréstimo de R${:.2f} em {} anos com uma parcela mensal de R${:.2f}'.format(valor_emprestimo,anos,valor_prestacao))

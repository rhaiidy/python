""" DESAFIO 013: Faça um algoritmo que leia o salário de um funcionário e 
mostre seu novo salário com 15% de aumento.
CÁLCULO DE REAJUSTE SALARIAL"""

salario_1 = float(input('Me diz qual o seu salário: R$'))
# reajuste = 15%
aumento = (15*salario_1)/100
salario_2 = salario_1 + aumento
print('O seu salário de R${}, com o reajuste de 15%, irá para R${}.' .format(salario_1,salario_2))


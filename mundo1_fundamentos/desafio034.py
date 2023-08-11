""" DESAFIO 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
*AUMENTOS MÚLTIPLOS*
"""
# > R$1250,00 aumento de 10%
# <= R$1250,00 aumento de 15%

salario = float(input('Digite seu salário: '))

if salario <= 1250.00:
    aumento_1 = ((salario * 15)/100) + salario 
    print('Você receberá "15%" de aumento e seu novo salário será de R${:.2f}'.format(aumento_1))
else:
    aumento_2 = ((salario * 10)/100) + salario
    print('Você receberá "10%" de aumento e seu novo salário será de R${:.2f}'.format(aumento_2))

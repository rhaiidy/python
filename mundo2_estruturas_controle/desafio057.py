""" DESAFIO 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso tenha digitado errado, peça a digitação novamente até ter um valor correto.
*VALIDAÇÃO DE DADOS*
"""

sexo = str(input('Digite o seu sexo: [M] ou [F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:  ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

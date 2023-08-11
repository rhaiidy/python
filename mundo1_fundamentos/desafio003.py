""" Desafio 003: Crie um script Python que leia dois números e tente mostrar a soma entre eles."""

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
soma = (numero_1 + numero_2)
print (soma)
print ('A soma vale', soma)
print (f'A soma dos números digitados é igual a {soma}')
print ('A soma entre {} e {} é igual a {}.' .format(numero_1,numero_2,soma))
print (f'A soma entre {numero_1} e {numero_2} é igual a {soma}')

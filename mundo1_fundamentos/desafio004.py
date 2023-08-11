""" Métodos de testes de tipos

n = input ('Digite algo: ')
print (n.isnumeric()) # pra saber se é um número      ---
print (n.isalpha()) # pra saber se tem letras         ---  são MÉTODOS de testes de tipos  
print (n.isalnum()) # pra saber se é alfanumérico     ---
"""

""" Desafio 004: Faça um programa que leia algo pelo teclado e 
mostre na tela o seu tipo primitivo e todas as informações possíveis. """

entrada = input ('Digite algo:')
print (f'Só tem espaços?', (entrada.isspace()))
#print ('Só tem espaços?', entrada.isspace()) # só pra mostrar a diferença sem F-string
print (f'É um número?', (entrada.isnumeric()))
print (f'É alfabético?', (entrada.isalpha()))
print (f'É alfanumérico?', (entrada.isalnum()))
print (f'Está em maiúsculas?', (entrada.isupper()))
print (f'Está em minúsculas?', (entrada.islower()))
print (f'Está capitalizada?', (entrada.istitle()))

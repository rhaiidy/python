""" Desafio 005: Criar um script em Python que mostre o antecessor
e o sucessor de um número digitado pelo usuário. """

n = int(input('Digite um número: '))
antecessor = n-1
sucessor = n+1
print(f'antecessor: {antecessor} , seu número: {n} , sucessor: {sucessor}')

"""
n = int(input('Digite um número: '))
antecessor = n-1                                
sucessor = n+1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}', format(n,antecessor,sucessor))

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,(n-1),(n+1)))
"""
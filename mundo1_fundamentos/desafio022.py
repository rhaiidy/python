""" DESAFIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras tem ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome

*ANALISADOR DE TEXTOS*
"""

nome = str(input('Digite seu nome completo: ')).strip()

# O nome com todas as letras maiúsculas
maiusculas = (nome.upper())
print('Seu nome em maiúsculas: {}' .format(maiusculas))
# O nome com todas as letras minúsculas
minusculas = (nome.lower())
print('Seu nome em minúsculas: {}' .format(minusculas))
# Quantas letras tem ao todo(sem considerar espaços)
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
# Quantas letras tem o primeiro nome
lista_nome = nome.split()
st_nome = (lista_nome[0])
qtd_letras_st_nome = (len(lista_nome[0]))
print('Seu primeiro nome é {} e ele tem {} letras' .format(st_nome,qtd_letras_st_nome))
print('Seu primeiro nome é {} e ele tem {} letras' .format(st_nome,nome.find(' ')))
print('Seu primeiro nome é {} e ele tem {} letras' .format(lista_nome[0],len(lista_nome[0])))


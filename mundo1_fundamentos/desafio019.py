""" DESAFIO 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo na tela o nome do escolhido.
 *SORTEANDO UM ITEM NA LISTA*
"""
import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O nome do aluno escolhido é: {}' .format(escolhido))

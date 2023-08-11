""" DESAFIO 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. 
*PROCURANDO UMA STRING DENTRO DA OUTRA*
"""
# achar a palavra SILVA em qualquer lugar da string

nome = str(input('Digite seu nome completo: ')).strip()
#print('Seu nome tem "SILVA"? {}'.format('silva' in nome.lower()))
print('Seu nome tem "SILVA"? {}'.format('SILVA' in nome.upper()))


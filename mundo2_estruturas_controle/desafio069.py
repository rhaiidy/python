""" DESAFIO 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos
b) Quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos.
*ANÁLISE DE DADOS DO GRUPO*
"""
a = b = c = 0
while True:
    print('~'*30)
    print('CADASTRE UMA PESSOA')
    print('~'*30)
    idade = int(input('Idade: '))
    if idade >=18:
        a += 1    
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M]  ')).strip().upper()[0]
        if sexo == 'M':
            b += 1
        if sexo == 'F' and idade < 20:
            c += 1 
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {a}')
print(f'Total de homens cadastrados: {b}')
print(f'Total de mulheres com menos de 20 anos: {c}')


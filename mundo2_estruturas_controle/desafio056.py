""" DESAFIO 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
- A média de idade do grupo
- Qual é nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
*ANALISADOR COMPLETO*
"""
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
totmulher20 = 0

for p in range(1,5): 
    print('►►►►► {}ª PESSOA ◄◄◄◄◄'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    soma_idade += idade
    if p == 1 and sexo in 'M':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
         
media_idade = soma_idade / 4 
print('A média de idade do grupo é de {}'.format(media_idade))    
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem,nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

      


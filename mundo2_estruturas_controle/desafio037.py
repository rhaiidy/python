""" DESAFIO 037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal 

*CONVERSOR DE BASES*
"""

n = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
escolha = int(input('Digite a opção escolhida: '))

if escolha == 1:
    print('{} convertido para BINÁRIO seria {}'.format(n,bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL seria {}'.format(n,oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL seria {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida! Tente novamente.')

# 0b = binário (zero b)
# 0o = octal
# 0x = hexadecimal
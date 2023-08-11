""" DESAFIO 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO 
*AQUELE CLÁSSICO DA MÉDIA*
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,m))

if m <5:
    print('REPROVADO!')
elif m >=5 and m <=7:    # pode ser tb: if 7 > m >=5
    print('RECUPERAÇÃO!')
elif m >=7:
    print('APROVADO!! PARABÉNS!!')
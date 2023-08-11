""" Desafio 011: Faça um programa que calcule a área de um cômodo e veja
quantos litros de tinta serão necessários para pintar todo o cômodo.
Considerações: cada litro de tinta pinta 2m². """

l = float(input('Digite a largura do cômodo em metros: '))
c = float(input('Digite o comprimento do cômodo em metros: '))
a = l*c
tinta = (a/2)
print('O comprimento do seu cômodo é de {:.1f}m, a largura é {:.1f}m e o valor total da área é de {}m².'.format(c,l,a))
print('Seriam necessários {:.1f} litros de tinta para pintar todos os {:.1f}m².' .format(tinta,a))

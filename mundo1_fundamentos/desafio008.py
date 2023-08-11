""" Desafio 008: Criar um programa que receba o valor em metros e 
mostrar pro usuario em centimetros e milimetros."""

m = float(input('Digite o valor em metros: '))
km = m /1000
hm = m/100
dam = m /10
dm = m *10
cm = m *100
mm = m *1000
print(f'{m}metros equivale a:\n{km}km\n{hm}hm\n{dam}dam\n{m}m\n{dm}dm\n{cm}cm\n{mm}mm')
#print('{}m equivale a {:.0f}cm e {:.0f}mm.' .format(m,cm,mm))
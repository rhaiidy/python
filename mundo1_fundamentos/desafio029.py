""" DESAFIO 029: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado.
A multa vai custar R$7.00 por cada km acima do limite. 

 *RADAR ELETRÔNICO*
"""

v = float(input('Digite a velocidade: '))
# Se a velocidade passar de 80km, mostre a msg dizendo que ele será multado.
if v >80:
    print('Você ultrapassou a velocidade permitida da via. Você será multado!')
    multa = (v - 80) * 7
    print('O valor da sua multa será de R${:.2f}'.format((multa)))
else:
    print('Sua velocidade está dentro do limite, não se preocupe.')




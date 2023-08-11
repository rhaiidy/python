""" DESAFIO 014: Faça um algoritmo que converta a temperatura de Celsius para Fahrenheit e Kelvin. 
*CONVERSOR DE TEMPERATURAS*
"""
celsius = float(input('Informa a temperatura em C°: '))
fahrenheit = ((celsius*9)/5) + 32
kelvin = (celsius + 273.15)
print('A temperatura de {}° corresponde à {}F e {}K.'.format(celsius,fahrenheit,kelvin))

 

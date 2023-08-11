""" DESAFIO 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu
status, de acordo com a tabela abaixo:
- Abaixo de 18.5 = abaixo do peso
- Entre 18.5 e 25 = peso ideal
- 25 até 30 = sobrepeso
- 30 até 40 = obesidade
- Acima de 40 = obesidade mórbida
*IMC*
"""
# IMC = peso / (altura x altura). resultado 
peso = float(input('Digite seu peso (em KG): '))
altura = float(input('Digite sua altura (em m): '))
imc = peso/(altura**2)
print(imc)

if imc < 18.5:
    print('O seu IMC é de {:.2f} e você está classificado(a) como "ABAIXO DO PESO".'.format(imc))
elif imc >= 18.5 and imc <25:
    print('O seu IMC é de {:.2f} e você está classificado(a) como "PESO IDEAL".'.format(imc))
elif imc >= 25 and imc <30:
    print('O seu IMC é de {:.2f} e você está classificado(a) com "SOBREPESO".'.format(imc))
elif imc >= 30 and imc <40:
    print('O seu IMC é de {:.2f} e você está classificado(a) como "OBESO".'.format(imc))
elif imc >= 40:
    print('O seu IMC é de {:.2f} e você está classificado(a) com "OBESIDADE MÓRBIDA".'.format(imc))
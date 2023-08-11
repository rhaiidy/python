""" DESAFIO 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
*TABUADA v3.0*
"""
n = c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('~'*30)
    for c in range(1,11):
        print(f'{n} x {c:2} = {n*c}')
    print('~'*30)
print('Programa TABUADA encerrado. Volte sempre.')
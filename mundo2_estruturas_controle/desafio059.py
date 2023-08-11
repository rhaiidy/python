""" DESAFIO 059: Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar 
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
*CRIANDO UM MENU DE OPÇÕES*
"""
from time import sleep
opcao = 0
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

while opcao !=5:  
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    opcao = int(input('→→→→→→→→→→ Qual sua opção? '))

    if opcao == 1:
        soma = primeiro + segundo
        print('A soma de {} e {} é igual a {}.'.format(primeiro,segundo,soma))
    elif opcao == 2:
        mult = primeiro * segundo
        print('O resultado de {} x {} é igual a {}.'.format(primeiro,segundo,mult))
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('Entre {} e {} o maior é {}.'.format(primeiro,segundo,maior))    
    elif opcao == 4:
        print('Informe novamente os valores: ')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('Opção inválida. ')
    print('=-='*10)
print('FIM DO PROGRAMA! ATÉ LOGO!')
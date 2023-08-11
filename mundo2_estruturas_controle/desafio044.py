""" DESAFIO 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- á vista - dinheiro ou cheque = 10% de desconto
- á vista no cartão = 5% de desconto
- em até 2x no cartão = preço normal
- 3x ou mais no cartão = 20% de juros
*GERENCIADOR DE PAGAMENTOS*
"""
"""(1)A VISTA NO DINHEIRO OU CHEQUE (2) A VISTA NO CARTÃO (3) PARCELADO 
se escolher parcelado : (1) 2x NO CARTÃO (2) 3x OU MAIS NO CARTÃO """

print('{:=^30}'.format(' LOJAS RHAIDYLAND '))
valor_inicial = float(input('Digite o valor do produto: R$'))
forma = str(input('Digite a forma de pagamento: \n (1) A VISTA NO DINHEIRO OU CHEQUE\n (2) A VISTA NO CARTÃO\n (3) PARCELADO\n'))

if forma == '1':
    desconto_10 = (valor_inicial*10)/100
    valor_final = valor_inicial - desconto_10
    print('O seu produto de R${:.2f} com "10%" de desconto sairá por R${:.2f}'.format(valor_inicial,valor_final))

if forma == '2':
    desconto_5 = (valor_inicial*5)/100
    valor_final = valor_inicial - desconto_5
    print('O seu produto de R${:.2f} com "5%" de desconto sairá por R${:.2f}'.format(valor_inicial,valor_final))

if forma == '3':
    forma_parcelamento = str(input('Como deseja parcelar? \n(1) 2x NO CARTÃO \n(2) 3x OU MAIS NO CARTÃO\n'))
    if forma_parcelamento == '1':
        duas_vezes = valor_inicial/2
        print('O seu produto de R${:.2f} sairá por 2x R${:.2f} sem juros.'.format(valor_inicial,duas_vezes))
    if forma_parcelamento == '2':
        juros_20 = (valor_inicial*20)/100
        valor_final = valor_inicial + juros_20
        print('O seu produto de R${:.2f} sairá por R${:.2f} com "20%" de juros.'.format(valor_inicial,valor_final))


""" DESAFIO 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
*SUPER PROGRESSÃO ARITMÉTICA v3.0*
"""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
c = 1
total = 0
mais_termos = 10    
while mais_termos != 0:
    total += mais_termos    
    while c <= total:
        print('{} → '.format(termo), end=' ')
        termo += razao
        c += 1 
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais?  '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

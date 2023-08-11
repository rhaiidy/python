""" Desafio 006: Criar um script em Python que mostre o dobro, triplo
e raiz quadrada de um número digitado pelo usuário. """

n_usuario = int(input('Digite um número: '))
dobro = n_usuario *2
triplo = n_usuario *3
raiz = n_usuario **(1/2)
#print(f'O dobro de {n_usuario} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz}.')
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}' .format(n_usuario,dobro,triplo,raiz))

from random import choice
print('=-'*25)
lista = []
titulo = 'SORTEIO'
print(titulo.center(50))
print('=-'*25)
qts=int(input('Quantos itens você quer sortear? :'))
for c in range(0,qts):
    c=str(input('Digite aqui:'))
    lista.append(c)
for v in range(0,qts):
    enter=str(input('\nDigite ENTER para sortear:'))
    sorteio=choice(lista)
    remover=lista.remove(sorteio)
    print('\033[1;97m{}\033[m'.format(sorteio))
    if v == qts:
        break
fim = '\033[1;34mFIM DO SORTEIO\033[m'
print('\033[1;34m=-\033[m'*25)
print(fim.center(50))
print('\033[1;34m=-\033[m'*25)
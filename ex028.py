from random import randint
from time import sleep
computador = randint(0,5)
print('Pensei no numero{}'.format(computador))
print('-=-' * 20)
print('Vou pensem em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que jogo eu pensei?? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no númeor {} e não no {}!'.format(computador, jogador))

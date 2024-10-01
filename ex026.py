frase = str(input('Digite uma frase: ')).strip().upper()

print('A primeira letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('Aúltima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
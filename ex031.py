distancia = float(input('Qual é a distância da sua viagem? '))
print('Voce está prestes a começar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

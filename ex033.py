a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {:.2f}'.format(menor))
print('O maior valor digitado foi: {:.2f}'.format(maior))

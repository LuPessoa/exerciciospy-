distancia = float(input('Qual a distância da viajem ?'))
if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de {}R$'.format(preco))

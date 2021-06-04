dias = float(input('Quantos dias ficou alugado?'))
km = float(input('Quantos Km o carro percorreu ?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

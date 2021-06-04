casa = float(input('valor da casa: R$'))
salario = float(input('Sálario do comprador : R$'))
anos = float(input('Quantos anos de financiameto?'))
prestaçao = casa/(anos * 12)
minimo = (30/100) * salario
print('Para pagar uma casa de R${:.2f} em {:.0f} anos'.format(casa, anos))
print('A prestação sera de {:.2f} R$'.format(prestaçao))
if prestaçao <= minimo:
    print('Empretismo pode ser CONCEDIDO!')
else:
    print("O empréstimo NEGADO!")
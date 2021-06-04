print('{:=^40}'.format(" Loja da LU "))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] `a vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x npo cartão
[ 4 ] 3x no cartão''')
opção = int(input('Qual e a opção?'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalpar = int(input('Quantas parcelas?'))
    parcela = total / totalpar
    print('Sua compra será parcelada em {}x de R${} com JUROS'.format(totalpar, parcela ))
else:
    total = preço
    print('\033[1;31;mOPÇÃO INVALIDA de pagamento. Tente novamente')
print('\033[1;34;mSua Compra de R${} vai custar R$ {:.2f} no final'.format(preço, total))




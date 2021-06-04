sal = float(input('Qual seu salário ?'))
re = sal*(15/100)
salf = sal + re
print('O salário de {}R$ coma ajuste de 15% vai para {:.2f}R$'.format(sal, salf))
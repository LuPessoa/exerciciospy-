sal = float(input('Qual o seu salário R$'))
if sal <= 1250:
    sal = ((15/100)* sal) + sal
    print(" O Salário recebeu aumento de 15% e foi para :{}R$".format(sal))
else:
    sal = (10/100 * sal)+sal
    print('O Salario recebeu aumento de 10% e foi para : {} R$'.format(sal))
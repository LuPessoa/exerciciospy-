from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento :'))
idade = atual - nasc
print('idade atual {}'.format(idade))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18 :
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18 :
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi no ano {}'.format(ano))
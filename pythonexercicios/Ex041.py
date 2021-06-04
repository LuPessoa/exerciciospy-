from datetime import date
ano = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Categória MIRIM')
elif idade  <= 14:
    print('Categória INFANTIL')
elif idade <= 19:
    print('Categória JÚNIOR')
elif idade <= 25:
    print('Categória SÊNIOR')
elif idade > 25:
    print('Categória MASTER')

a = int(input('\033[0;35;mDigite o primeiro valor :'))
b = int(input('\033[0;33mDigite o segundo valor:'))
c = int(input('\033[031mDigite o terceiro valor:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('\033[0;32mO menor valor digitado foi {}'.format(menor))
print('\033[0;35mO maior valor digitado foi {}'.format(maior))

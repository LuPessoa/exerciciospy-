expr = str(input('Dogite a sua expressão:'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif len(pilha) > 0:
        pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha) == 0:
        print('Sua expressão está valida :')
else:
        print('Sua expressão está Invalida')



def leiaInt(msg):
    '''

    :param msg:
    :return:
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
        if ok:
            break
    return valor
#programa principal
n = int(leiaInt('Digite um numero :'))
print(f'Você digitou o numero {n}')

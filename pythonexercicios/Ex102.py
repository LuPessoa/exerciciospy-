def fatorial(n, show=False):
    """"

    -> Calcular fatorial de um numero:
    :parametro n :O número a ser calculado.
    :parametro show : (opcional)Mostrar ou não a conta.
    :return: O valor do fatorialde um numero n.
    """


    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1 :
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *=c
    return f

#programa principal
print(fatorial(5, show=True))
help(fatorial)
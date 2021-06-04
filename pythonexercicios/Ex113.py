def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[031mERRO!Por favor, Digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[031mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\n\033[031mERRO:Por Favor, Difite um numero real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[031mERRO:Usuario preferiu não digitar um número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real:')
print(f'O valor Digitado foi {n1} e {n2}')
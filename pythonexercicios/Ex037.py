num = int(input('Digite um numero inteiro :'))
print('''Escolha uma das bases para conversão :
[ 1 ] Converter para BINÁRIO
[ 2 ] Conveter para OCTAL
[ 3 ] Coverter para HEXADECIMAL''')
opçao = int(input('Sua opção:'))
if opçao == 1 :
    print('{} Convertido para BINÁRIO e igual a {} '.format(num, bin(num)[2:]))
elif opçao == 2 :
    print('{} Convertido Para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} Convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente novamente.')
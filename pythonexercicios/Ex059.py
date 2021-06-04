from time import sleep
n1 = int(input('Digite o primeiro valor :'))
n2 = int(input('Digite o segundo valor :'))
opção = 0
while opção !=5:
    print('''   [ 1 ] Soma
    [ 2 ]multiplicar
    [ 3 ]maior
    [ 4 ]novos numeros 
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>> Qual e a sua opção ?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} e {} e {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os novos numeros:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Dados Inválidos. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa, Volte sempre')

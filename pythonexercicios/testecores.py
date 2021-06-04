'''\033[0;30;41m]
\033[4;33;44m]
\033[1;35;43m]negrito
\033[;30;42m]
\033[m #sem configuração
\033[7;30 #inverte'''
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[0;33;44mLucilene Pessoa Macedo')
print('\033[7;33;45mPai : João Alves Pessoa!\033[m')
nome = 'Lucilene'
cores = {'limpa':'\033[n',
         'Azul':'\033[34m',
         'Amarelo':'\033[33m',
        'Pretobranco':'\033[7;30m]'}
print('Olá, Muito prazer em te conhecer :{}{}{}!!!'.format(cores['Amarelo'],nome, '\033[7;36'))
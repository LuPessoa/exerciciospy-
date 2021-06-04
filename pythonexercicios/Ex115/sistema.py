from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExist(arq):
    criarArquivo(arq)

while True:
   resposta = menu(['Ver pessoa Cadastradas','Cadastrar nova pessoa','Sair do sitema'])
   if resposta == 1:
       #Oção de listar o conteudo de um arquivo!
       lerArquivo(arq)
   elif resposta == 2:
       #opçãode cadastras uma nova pessoa.
       cabeçalho('NOVO CADASTRO')
       nome = str(input('Nome: '))
       idade = leiaInt('Idade: ')
       cadastrar(arq, nome, idade)
   elif resposta == 3:
       cabeçalho('Saindo do sistema...Até logo!')
       break
   else:
       print('\033[31mDigite uma Opção válida\033[m')
   sleep(2)
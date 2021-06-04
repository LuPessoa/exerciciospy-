questão 1
def linhas_de(nome_arquivo, remover_sep_pag = bool()):
    linhas = []
    with open(nome_arquivo, mode='r') as arquivo:
        linha = '*' # leia toto arquivo
        while linha != '': # enquanto texto leia proxima linha
            linha = arquivo.readline()
             # se usuario não escrever nada ou false
            if remover_sep_pag == False:
                # ler todas as linhas
               if linha != '':
                   linhas.append(linha.replace('\n', ''))
            else:
                linha != '' and linha != '\n':
                linhas.append(linha(replace))

            return linhas


        linhas_de('A princess of Mars-Edgar Rice Burrounghs.txt')



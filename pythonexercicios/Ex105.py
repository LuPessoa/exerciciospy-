def notas(*n, sit=False):
    """"
    -> Função para analisar notas e situações de varios alunos.
    :param n:uma ou mais notas dos alunos (aceita varias)
    :param sit:valor opcional, indicando se deve ou não adcionar situação.
    :return: dicionário com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
           r['situação'] = 'BOA'
        elif r['media'] >= 5:
           r['situação'] = 'Razoavel'
        else:
           r['Situação'] = 'Ruim'
    return r

#programa Principal
resp = notas(5.5, 9, 1.5, sit=True)
print(resp)
help(notas)
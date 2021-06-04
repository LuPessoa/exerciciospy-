vel = float(input('Qual a velocidade do carro ?'))
if vel >80:
    print('Você ultrapassou a velocidade maxima permitida, será multado')
    mul = (vel-80)*7
    print('Você deve pagar uma multa de {}'.format(mul))
print('Tenha um bom dia! dirija com segurança!')
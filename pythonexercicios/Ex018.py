import math
an = float(input('Digite o Angulo:'))
seno = math.sin(math.radians(an))
coseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O Angulo  de {}\n Tem o SENO de {:.2f} \nO COSENO de {:.2f}\n O TANGENTE {:.2f}'.format(an, seno, coseno, tangente))
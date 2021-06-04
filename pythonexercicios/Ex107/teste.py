from Ex107 import moeda

p = float(input('Digite o preço R$:'))
print(f'A metade do {p} é {moeda.metade(p)}')
print(f'O dobro do {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 20% de {p}R$ é {moeda.diminuir(p, 20)}')
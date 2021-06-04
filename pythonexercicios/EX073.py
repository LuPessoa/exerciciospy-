times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avai', 'Ponte Preta ', 'Atetico - GO')
print('=-' *20)
print(f'Lista de times Brasileirão {times}')
print('=-'*20)
print(f'Os cinco Primeiros Times São : {times[:5 ]}')
print('=-'*10)
print(f'Os ultimos quatro colocados são : {times[-4 :]}')
print('=-'*20)
print(f'Times em ordem Alfabetica : {sorted(times)}')
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
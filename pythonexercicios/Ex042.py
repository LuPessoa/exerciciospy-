l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo seguimento:'))
l3 = float(input('Terceiro Segmento:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima podem formar um triângulo',end=' ')
    if l1 == l2 == l3:
        print('EQUILÀTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
     print('Os segmentos acima não podem forma um triangulo')

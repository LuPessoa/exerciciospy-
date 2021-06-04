import math
co = float(input("Qual o comprimento do cateto ?"))
ca = float(input("Qual o cateto adjcente ?"))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))
#com calculo
co = float(input("Qual o comprimento do cateto ?"))
ca = float(input("Qual o cateto adjcente ?"))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))


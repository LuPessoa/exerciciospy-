import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
   print('o site Pudim não está acesivel no momento.')
else:
   print('Consegui acessar o site Pudim com Sucesso!')
   print(site.read())
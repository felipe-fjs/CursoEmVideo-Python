import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://google.com/')
except urllib.error.URLError:
    print(f'\033[1;31mNão conseguir acessar \033[4;35m{'www.pudim.com.br'}\033[m\033[1;31m!\033[m')
else:
    print(f'Conseguir acessar o pudim!')

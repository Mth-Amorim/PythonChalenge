import urllib.request
import re
import datetime

def proxima_url(url):
    conteudo = urllib.request.urlopen(url)
    conteudo = conteudo.read()
    numeros_encontrados = "".join(re.findall(r'\d+', str(conteudo)))
    if numeros_encontrados != "":
        nova_url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={numeros_encontrados}"
        return (True , nova_url)
    else:
        return (False, url)


url_inicial = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
nova_url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
nova_url = url_inicial

inicio =  datetime.datetime.now()
while True:
    url = proxima_url(nova_url)
    if url[0]:
        nova_url = url[1]
        print(f"{nova_url}")
    else:
        break

Fim =  datetime.datetime.now()
print('Tempo foi de : {}'.format(Fim - inicio))
print(nova_url)

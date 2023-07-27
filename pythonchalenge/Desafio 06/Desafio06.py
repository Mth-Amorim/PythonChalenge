import pickle
import urllib.request

# Pegando o dado - Parte 01
dados = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
dados_deserializados = pickle.load(dados) 

# Conferidno se todas as litas  os numeros são iguais 
# valor = 0
# for listas in dados_deserializados:
#     for itens in listas:
#         valor = valor + itens[1]
#     if valor == 95:
#         valor=0
#         print(itens)
#     else:
#         print(listas)
#         raise('Valor não bate')

# Printando as litas uma em cada linha 


for listas in dados_deserializados:
    linha = ""
    for letra, quantidade in listas:
        linha = linha + "".join(letra * quantidade)
    print(linha)

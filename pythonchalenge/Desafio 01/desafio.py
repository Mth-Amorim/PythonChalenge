texto_inicial = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

# Tentativa 01 
texto_inicial = texto_inicial.upper().replace('K', 'M')
texto_inicial = texto_inicial.upper().replace('O', 'Q')
texto_inicial = texto_inicial.upper().replace('E', 'G')
print(texto_inicial)


# Tentativa 02 
# Contando os caracteres 
dicionario = {}
for letra in texto_inicial:
    if letra in dicionario.keys():
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

# Classificando em ordem de ocorrencia 
dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: (item[1]), reverse=True))
print(dicionario_ordenado)

# Tentativa 03 
# Trocando caracteres duas csas para frente 
texto_inicial = texto_inicial.upper()
Texto_novo = ""
for letra in texto_inicial:
    letra_antiga = ord(letra)
    letra_nova = chr(letra_antiga + 2)
    Texto_novo = Texto_novo + letra_nova
print(Texto_novo)

# Tentativa 04 
# As letras na tabela ASC2 Iniciam apartir da letra 65 .... 
# No for só pode aplicar a correção se o retorno do asc for entre 65 e 90
 
texto_inicial = texto_inicial.upper()
Texto_novo = ""
for letra in texto_inicial:
    letra_antiga = ord(letra)
    if letra_antiga>=65 and letra_antiga<=90:
        letra_nova = (letra_antiga - 65 + 2) % 26 + 65
        Texto_novo = Texto_novo + chr(letra_nova)
    else:
        Texto_novo = Texto_novo + letra
print(Texto_novo)


url = 'MAP'
Texto_novo = ""
for letra in url:
    letra_antiga = ord(letra)
    if letra_antiga>=65 and letra_antiga<=90:
        letra_nova = (letra_antiga - 65 + 2) % 26 + 65
        Texto_novo = Texto_novo + chr(letra_nova)
    else:
        Texto_novo = Texto_novo + letra
print(Texto_novo)


# Resolução official da agina 
import string

texto_inicial = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

tabela = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
texto_criptografado = texto_inicial.translate(tabela)

print(texto_criptografado)

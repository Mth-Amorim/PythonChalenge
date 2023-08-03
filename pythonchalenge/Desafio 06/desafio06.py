from pathlib import Path
import zipfile

# desafio 07  
# Percorrer todos os TXT's que se encontram na pasta 

pasta = Path(r'C:\Users\Matheus\Downloads\Nova pasta')# Trocar para a pasta com os arquivosa zipados 
lista_arquivos = pasta.glob(pattern='*.txt')

file_path = Path(pasta, '90052.txt') 

for arquivo in lista_arquivos:
    with open(arquivo,'r') as arquivo_txt:
        texto = arquivo_txt.read()

    if "Next nothing is" not in texto: 
        print(f"Arquivo: {arquivo}")
        print(f'Texto: {texto}')

# Tentativa 02 
caminho_zip = Path(pasta, 'channel.zip')
arquivo_zip = zipfile.ZipFile(caminho_zip,'r')

numero = '90052'
comentarios = []
while True:
    conteudo = arquivo_zip.read(f'{numero}.txt').decode('utf-8')
    comentarios.append(arquivo_zip.getinfo(f'{numero}.txt').comment.decode('UTF-8'))
    if "Next nothing is" not in conteudo: 
        print(f"Arquivo: {numero}.txt")
        print(f'Texto: {conteudo}')
        break
    else: 
        conteudo = conteudo.split(' ')
        numero = conteudo[-1]
comentarios = "".join(comentarios)
print(comentarios)

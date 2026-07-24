import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'

requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text,'html.parser')

# print(extracao.text.strip())

for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):

    if linha_texto.name == 'h2':
        contar_titulos += 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('Total de títulos: ', contar_titulos)
print('Total de paragrafos: ', contar_paragrafos)

for linha_texto in extracao.find_all(['h1', 'p']):
    if linha_texto.name == 'h1':
        titulo = linha_texto.text.strip()
        print('Titulo: \n', titulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)
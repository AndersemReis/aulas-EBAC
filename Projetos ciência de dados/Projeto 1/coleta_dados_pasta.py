#https://finance.yahoo.com/quote/%5EBVSP/history
import pandas as pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

# Teste com a URL simplificada primeiro
url = 'https://finance.yahoo.com/quote/%5EBVSP/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

try:
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        print("Sucesso! Conectado ao Yahoo Finance.")
        print(f"Início do HTML: {response.text[:50]}")
    else:
        print(f"Erro {response.status_code}: O Yahoo recusou o acesso a esta URL específica.")

except Exception as e:
    print(f"Erro de conexão: {e}")

html_buffer = StringIO(response.text)

# 2. Lemos a tabela a partir do conteúdo que o 'requests' já baixou
url_dados = pd.read_html(html_buffer)

soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

url_dados = pandas.read_html(url_dados)
print(url_dados[0].head(10))
from pathlib import Path
import requests
import pandas as pd

# Mudança na URL: O parâmetro esperado por esta função específica do BCB é 'DataBase' (com B maiúsculo) 
# ou simplesmente passado como parâmetro de consulta.
URL = "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)"

PARAMS = {
    "@DataBase": "'202412'", # Testando com Dezembro/2024
    "$format": "json",
    "$top": 1000000
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, params=PARAMS, headers=headers, timeout=30)
    print(f"URL testada: {response.url}")
    
    response.raise_for_status()
    dados = response.json().get("value", [])
    
    if not dados:
        print("A lista 'value' veio vazia. Verifique se o mês 202412 já possui dados.")
    else:
        df = pd.DataFrame(dados)
        print(f"Sucesso! {len(df)} linhas carregadas.")
        
        OUTDIR = Path(r"C:\Users\Familia_Souza\OneDrive\Documentos\Aulas EBAC\Projetos ciência de dados\data\raw")
        OUTDIR.mkdir(parents=True, exist_ok=True)
        df.to_csv(OUTDIR / "pix_municipio_correto.csv", index=False, encoding="utf-8-sig")
        print("Arquivo salvo com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
    if 'response' in locals():
        print(f"Resposta do servidor: {response.text}")
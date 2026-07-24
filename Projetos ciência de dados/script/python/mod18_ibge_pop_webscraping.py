from pathlib import Path
import requests

XLS_URL = "https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260113.xls"

resp = requests.get(XLS_URL,stream=True,timeout=60)
resp.raise_for_status()

OUTDIR = Path(r"C:\Users\Familia_Souza\OneDrive\Documentos\Aulas EBAC\Projetos ciência de dados\data\raw")
OUTDIR.mkdir(parents=True, exist_ok=True)

XLS_LOCAL = OUTDIR / "pop_ibge_2025.xls"

with open(XLS_LOCAL, "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("Arquivo salvo em: ", XLS_LOCAL)
import requests

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL
)


def analisar_vaga(descricao):

    prompt = f"""
Você é um recrutador especialista.

Analise esta vaga.

Dê uma nota de 0 a 100.

Explique os motivos.

Vaga:

{descricao}
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    if resposta.status_code != 200:
        return "Erro ao consultar o Ollama."

    return resposta.json()["response"]
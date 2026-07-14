import requests

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL,
)


def analisar_vaga(descricao):

    prompt = f"""
Você é um especialista em recrutamento.

Analise esta vaga.

Retorne SOMENTE um número de 0 até 100.

Descrição:

{descricao}
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    texto = resposta.json()["response"].strip()

    try:
        nota = int("".join(filter(str.isdigit, texto)))
    except:
        nota = 0

    if nota > 100:
        nota = 100

    return nota
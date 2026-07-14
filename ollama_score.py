import requests

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL,
)


def analisar_vaga(descricao):

    prompt = f"""
Você é um especialista em recrutamento.

Analise esta vaga.

Dê uma nota de 0 a 100 considerando:

- Qualidade
- ISO
- Auditoria
- Processos
- Melhoria Contínua
- Assistente de Qualidade
- Analista de Qualidade

Responda SOMENTE neste formato:

NOTA: 85

MOTIVO:
texto

VAGA:

{descricao}
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
    )

    return resposta.json()["response"]
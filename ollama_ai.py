"""
==========================================================
AUTOCURRICULO IA
MÓDULO OLLAMA
==========================================================
"""

import json
import requests

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL,
    TEMPERATURE,
)


def analisar_vaga(descricao):

    prompt = f"""
Você é um especialista em recrutamento.

Analise a vaga abaixo.

Dê uma nota de 0 a 100 para compatibilidade com um profissional de Qualidade.

Considere:

- Assistente de Qualidade
- Analista de Qualidade
- ISO
- Auditoria
- Inspeção
- Controle de Qualidade
- Processos
- Melhoria Contínua
- Ferramentas da Qualidade

Responda SOMENTE neste formato:

NOTA: xx

JUSTIFICATIVA:
texto...

VAGA:

{descricao}
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE
        }
    }

    try:

        resposta = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        resposta.raise_for_status()

        dados = resposta.json()

        texto = dados["response"]

        nota = 0

        for linha in texto.splitlines():

            if "NOTA" in linha.upper():

                numeros = "".join(c for c in linha if c.isdigit())

                if numeros:

                    nota = int(numeros)

                    break

        return nota, texto

    except Exception as erro:

        print("Erro Ollama:", erro)

        return 0, "Erro na IA"


# ==========================================================
# TESTE
# ==========================================================

if __name__ == "__main__":

    descricao = """
Empresa procura Assistente de Qualidade.

Conhecimentos em ISO 9001,
auditorias internas,
controle de qualidade,
melhoria contínua,
5S e indicadores.
"""

    nota, resposta = analisar_vaga(descricao)

    print()

    print("=" * 60)

    print("NOTA:", nota)

    print()

    print(resposta)

    print("=" * 60)
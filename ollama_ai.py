"""
==========================================================
AUTOCURRICULO IA
MÓDULO OLLAMA
==========================================================
"""

import requests

from config import (
    OLLAMA_URL,
    OLLAMA_MODEL,
    TEMPERATURE,
)


# ==========================================================
# ANALISA UMA VAGA
# ==========================================================

def analisar_vaga(descricao):

    # Limita o tamanho da descrição para acelerar a IA
    descricao = descricao[:1800]

    prompt = f"""
Analise esta vaga para um profissional de Gestão da Qualidade.

Avalie a compatibilidade considerando conhecimentos em:

- Assistente de Qualidade
- Analista de Qualidade
- ISO 9001
- Auditorias
- Inspeção
- Controle de Qualidade
- Processos
- Melhoria Contínua
- Ferramentas da Qualidade

Responda EXATAMENTE neste formato:

NOTA: XX

JUSTIFICATIVA:
Até 3 linhas.

VAGA:

{descricao}
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE,
            "num_predict": 120
        }
    }

    try:

        resposta = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        if resposta.status_code != 200:
            print(f"Status: {resposta.status_code}")
            print(f"Resposta: {resposta.text}")
            return 0, "Erro na IA"

        dados = resposta.json()

        texto = dados.get("response", "")

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

Conhecimentos em:

- ISO 9001
- Auditorias internas
- Controle de qualidade
- Indicadores
- Melhoria contínua
- 5S
"""

    nota, resposta = analisar_vaga(descricao)

    print("\n" + "=" * 60)
    print("NOTA:", nota)
    print("=" * 60)
    print(resposta)
    print("=" * 60)
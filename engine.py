"""
==========================================================
AUTOCURRICULO IA
ENGINE
==========================================================
Motor responsável por classificar e priorizar vagas.
"""

import logging


# ==========================================================
# SCORE FINAL
# ==========================================================

def calcular_score_final(score_palavras, score_ia):
    """
    Combina o score por palavras com o score da IA.
    """

    return round((score_ia * 0.8) + (score_palavras * 0.2))


# ==========================================================
# PRIORIDADE
# ==========================================================

def definir_prioridade(score_final):

    if score_final >= 80:
        return "ALTA"

    if score_final >= 60:
        return "MEDIA"

    if score_final >= 40:
        return "BAIXA"

    return "DESCARTAR"


# ==========================================================
# LOG
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
# ==========================================================
# PROCESSA TODAS AS VAGAS
# ==========================================================

def processar_vagas(vagas):

    logging.info("=" * 60)
    logging.info("PROCESSANDO VAGAS")
    logging.info("=" * 60)

    vagas_processadas = []

    for vaga in vagas:

        try:

            score_palavras = vaga.get("score", 0)
            score_ia = vaga.get("score_ia", 0)

            score_final = calcular_score_final(
                score_palavras,
                score_ia
            )

            prioridade = definir_prioridade(
                score_final
            )

            vaga["score_final"] = score_final
            vaga["prioridade"] = prioridade

            vagas_processadas.append(vaga)

            logging.info(
                f"{vaga.get('titulo')} | "
                f"Palavras={score_palavras} | "
                f"IA={score_ia} | "
                f"Final={score_final} | "
                f"{prioridade}"
            )

        except Exception as e:

            logging.error(
                f"Erro ao processar vaga: {e}"
            )

    # ======================================================
    # ORDENA DO MAIOR SCORE PARA O MENOR
    # ======================================================

    vagas_processadas.sort(
        key=lambda x: x["score_final"],
        reverse=True
    )

    logging.info("=" * 60)
    logging.info(
        f"{len(vagas_processadas)} vagas classificadas."
    )
    logging.info("=" * 60)

    return vagas_processadas
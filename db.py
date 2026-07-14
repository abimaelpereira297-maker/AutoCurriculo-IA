"""
==========================================================
AUTOCURRICULO IA
BANCO DE DADOS
==========================================================
"""

import sqlite3

DB_NAME = "vagas.db"


# ==========================================================
# CONEXÃO
# ==========================================================

def conectar():
    return sqlite3.connect(DB_NAME)


# ==========================================================
# CRIA O BANCO
# ==========================================================

def criar_banco():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vagas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            link TEXT UNIQUE,

            titulo TEXT,
            empresa TEXT,
            local TEXT,

            descricao TEXT,

            score INTEGER,
            score_ia INTEGER,
            score_final INTEGER,

            prioridade TEXT,

            analise_ia TEXT,

            curriculo TEXT,
            carta TEXT,

            candidatura TEXT,

            data TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("✅ Banco de dados pronto.")


# ==========================================================
# SALVAR VAGA
# ==========================================================

def salvar_vaga(
    link,
    titulo,
    empresa,
    local,
    descricao,
    score,
    score_ia,
    analise_ia,
    data
):

    score_final = round((score_ia * 0.8) + (score * 0.2))

    if score_final >= 80:
        prioridade = "ALTA"
    elif score_final >= 60:
        prioridade = "MEDIA"
    elif score_final >= 40:
        prioridade = "BAIXA"
    else:
        prioridade = "DESCARTAR"

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO vagas (

            link,
            titulo,
            empresa,
            local,
            descricao,

            score,
            score_ia,
            score_final,

            prioridade,

            analise_ia,

            curriculo,
            carta,
            candidatura,

            data

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        link,
        titulo,
        empresa,
        local,
        descricao,

        score,
        score_ia,
        score_final,

        prioridade,

        analise_ia,

        "",
        "",
        "PENDENTE",

        data

    ))

    conn.commit()
    conn.close()

    print(f"✅ Vaga salva: {titulo}")


# ==========================================================
# CONTAR VAGAS
# ==========================================================

def contar_vagas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM vagas")

    total = cursor.fetchone()[0]

    conn.close()

    return total
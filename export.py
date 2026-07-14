import sqlite3
import pandas as pd

DB_NAME = "vagas.db"


def gerar_excel():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query("""

        SELECT

            titulo,
            empresa,
            local,
            score,
            score_ia,
            ROUND((score_ia * 0.8) + (score * 0.2), 0) AS score_final,

            CASE
                WHEN ((score_ia * 0.8) + (score * 0.2)) >= 80 THEN 'ALTA'
                WHEN ((score_ia * 0.8) + (score * 0.2)) >= 60 THEN 'MEDIA'
                WHEN ((score_ia * 0.8) + (score * 0.2)) >= 40 THEN 'BAIXA'
                ELSE 'DESCARTAR'
            END AS prioridade,

            data,
            link,
            descricao,
            analise_ia

        FROM vagas

        ORDER BY score_final DESC

    """, conn)

    conn.close()

    arquivo = "vagas.xlsx"

    df.to_excel(
        arquivo,
        index=False
    )

    print("\n✅ Excel gerado com sucesso.")
    print(f"Arquivo: {arquivo}")
    print(f"Total de vagas: {len(df)}")


if __name__ == "__main__":
    gerar_excel()
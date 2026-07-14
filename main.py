"""
============================================================
AUTOCURRICULO IA
============================================================
"""

from linkedin import buscar_vagas
from engine import processar_vagas
from export import gerar_excel


def main():

    print("=" * 60)
    print("AUTOCURRICULO IA")
    print("=" * 60)

    vagas = buscar_vagas()

    print(f"\nForam coletadas {len(vagas)} vagas.")

    vagas = processar_vagas(vagas)

    print("\nGerando Excel...")

    gerar_excel()

    print("\nProcesso finalizado com sucesso.")


if __name__ == "__main__":
    main()
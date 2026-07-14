from playwright.sync_api import sync_playwright
from urllib.parse import quote
from datetime import datetime

from config import (
    PALAVRAS_CHAVE,
    CIDADES,
    CHROME_PROFILE,
    HEADLESS,
    MAX_VAGAS,
)

from db import (
    criar_banco,
    salvar_vaga,
    contar_vagas,
)

from ollama_ai import analisar_vaga


# ==========================================================
# SCORE POR PALAVRAS
# ==========================================================

def calcular_score(texto):

    texto = texto.lower()

    positivas = [
        "qualidade",
        "assistente",
        "analista",
        "inspeção",
        "controle",
        "iso",
        "auditoria",
        "processo",
        "melhoria",
        "5s",
        "indicadores",
        "não conformidade",
    ]

    negativas = [
        "estágio",
        "trainee",
        "júnior sem experiência",
    ]

    score = 0
    palavras = []

    for palavra in positivas:

        if palavra in texto:

            score += 2
            palavras.append("+ " + palavra)

    for palavra in negativas:

        if palavra in texto:

            score -= 3
            palavras.append("- " + palavra)

    return score, palavras


# ==========================================================
# LEITOR SEGURO
# ==========================================================

def obter_texto(page, seletor, primeiro=False):

    try:

        elemento = page.locator(seletor)

        if primeiro:
            elemento = elemento.first

        if elemento.count() == 0:
            return ""

        return elemento.inner_text().strip()

    except:

        return ""
# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def buscar_vagas():

    criar_banco()

    vagas_coletadas = []
    links_vistos = set()

    with sync_playwright() as p:

        print("=" * 60)
        print("INICIANDO ROBÔ")
        print("=" * 60)

        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(CHROME_PROFILE),
            headless=HEADLESS,
        )

        page = browser.pages[0] if browser.pages else browser.new_page()

        print("\nAbrindo LinkedIn...")

        page.goto(
            "https://www.linkedin.com/login",
            wait_until="domcontentloaded"
        )

        input("\n👉 Faça login e pressione ENTER para continuar...")

        palavra = PALAVRAS_CHAVE[0]
        cidade = CIDADES[0]

        url = (
            "https://www.linkedin.com/jobs/search/"
            f"?keywords={quote(palavra)}"
            f"&location={quote(cidade)}"
        )

        print("\nPesquisando vagas...")
        print(f"Cargo : {palavra}")
        print(f"Cidade: {cidade}")

        page.goto(
            url,
            wait_until="domcontentloaded"
        )

        page.wait_for_selector(
            "div.job-card-list__entity-lockup",
            timeout=30000
        )

        print("\nCarregando vagas...\n")
        ultimo_total = 0

        for scroll in range(30):

            page.mouse.wheel(0, 5000)

            page.wait_for_timeout(2000)

            cards = page.locator(
                "div.job-card-list__entity-lockup"
            )

            total = cards.count()

            print(
                f"Rolagem {scroll + 1}: {total} vagas carregadas"
            )

            if total == ultimo_total:
                break

            ultimo_total = total

        print(f"\nTotal encontrado: {ultimo_total}")

        cards = page.locator(
            "div.job-card-list__entity-lockup"
        )

        total = cards.count()

        print("\nIniciando coleta...\n")
        # ==========================================================
        # COLETA DAS VAGAS
        # ==========================================================

        for i in range(min(total, MAX_VAGAS)):

            try:

                card = cards.nth(i)

                card.scroll_into_view_if_needed()

                page.wait_for_timeout(800)

                card.click()

                page.wait_for_timeout(3000)

                titulo = obter_texto(
                    page,
                    ".job-details-jobs-unified-top-card__job-title h1"
                )

                empresa = obter_texto(
                    page,
                    ".job-details-jobs-unified-top-card__company-name a"
                )

                local = obter_texto(
                    page,
                    ".job-details-jobs-unified-top-card__primary-description-container span",
                    primeiro=True
                )

                descricao = obter_texto(
                    page,
                    "#job-details"
                )

                link = page.url

                if not titulo:
                    continue

                if link in links_vistos:
                    continue

                links_vistos.add(link)

                score, palavras = calcular_score(descricao)

                data = datetime.now().strftime("%d/%m/%Y %H:%M")

                # ==========================================================
                # ANÁLISE DA IA
                # ==========================================================

                score_ia, analise_ia = analisar_vaga(descricao)

                print(f"🤖 Score IA: {score_ia}")

                salvar_vaga(
                    link,
                    titulo,
                    empresa,
                    local,
                    descricao,
                    score,
                    score_ia,
                    analise_ia,
                    data
                )

                vagas_coletadas.append({

                    "titulo": titulo,
                    "empresa": empresa,
                    "local": local,
                    "descricao": descricao,
                    "link": link,
                    "score": score,
                    "score_ia": score_ia,
                    "analise_ia": analise_ia,
                    "palavras": palavras,
                    "data": data

                })

                print("\n" + "=" * 70)
                print(f"Vaga {i + 1}")
                print("=" * 70)
                print("Título :", titulo)
                print("Empresa:", empresa)
                print("Local  :", local)
                print("Score Palavras:", score)
                print("Score IA:", score_ia)
                print("Palavras:", ", ".join(palavras) if palavras else "Nenhuma")
                print("Descrição:")
                print(descricao[:300] + "..." if len(descricao) > 300 else descricao)
                print("Link:", link)

            except Exception as e:

                print(f"\nErro ao processar vaga {i + 1}: {e}")

                continue

        # ==========================================================
        # FIM DA COLETA
        # ==========================================================

        browser.close()

    print("\n" + "=" * 60)
    print("COLETA FINALIZADA")
    print("=" * 60)
    print(f"Vagas coletadas : {len(vagas_coletadas)}")
    print(f"Total no banco  : {contar_vagas()}")
    print("=" * 60)

    return vagas_coletadas


# ==========================================================
# EXECUÇÃO DIRETA
# ==========================================================

if __name__ == "__main__":
    buscar_vagas()
from playwright.sync_api import sync_playwright
import os

USER_DATA = os.path.join(os.getcwd(), "perfil")

with sync_playwright() as p:

    browser = p.chromium.launch_persistent_context(
        user_data_dir=USER_DATA,
        headless=False
    )

    page = browser.pages[0] if browser.pages else browser.new_page()

    input("Abra a página de vagas do LinkedIn e pressione ENTER...")

    print("\n===== TODOS OS LINKS DA PÁGINA =====\n")

    links = page.locator("a").all()

    for i, link in enumerate(links):

        try:
            href = link.get_attribute("href")
            texto = link.inner_text()

            print(i)
            print(texto)
            print(href)
            print("-" * 50)

        except:
            pass

    input("\nENTER para fechar")

    browser.close()
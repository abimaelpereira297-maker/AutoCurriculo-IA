from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    page = browser.new_page()

    page.goto(
        "https://www.linkedin.com/login",
        wait_until="domcontentloaded",
        timeout=60000
    )

    print("TÍTULO:", page.title())

    input("Pressione ENTER para fechar...")

    browser.close()
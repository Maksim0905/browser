from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://alphabet-physics.ru/")
    while True:
        page.reload()

with sync_playwright() as playwright:
    run(playwright)
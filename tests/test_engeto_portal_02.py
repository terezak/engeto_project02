from playwright.sync_api import Page, expect


BASE_URL = "https://portal.engeto.com/lobby/sign-in"
VALID_EMAIL = "valid@example.com"
VALID_PASSWORD = "validpassword"
INVALID_EMAIL = "invalid@example.com"
INVALID_PASSWORD = "invalidpassword"


def test_login_page_title(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("button", name="Přihlásit se pomoci e-mailu a").click()
    expect(page).to_have_title('Přihlášení | ENGETO')
    

#wrong password
def test_invalid_login_shows_error_message(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("button", name="Přihlásit se pomoci e-mailu a").click()

    page.locator("#username").fill(INVALID_EMAIL)
    page.locator("#password").fill(INVALID_PASSWORD)

    page.get_by_role("button", name="Pokračovat").click()  
    expect(page.locator("#error-element-password")).to_have_text('Nesprávný e-mail nebo heslo')

# # Test: Úspěšné přihlášení
# def test_successful_login(page):
#     page.get_by_role("button", name="Přihlásit se pomoci e-mailu a").click()
#     page.fill("input[name='email']", VALID_EMAIL)
#     page.fill("input[name='password']", VALID_PASSWORD)
#     page.click("button[type='submit']")
#     page.wait_for_url("**/dashboard")  # Ověření přesměrování
#     assert "dashboard" in page.url

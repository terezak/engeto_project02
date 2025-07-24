import re
from playwright.sync_api import Page, expect

BASE_URL = "https://engeto.cz/"

# def test_click_cookies_reject(page: Page):
#     """Testing cookies on the active page in case they are reactivated.""" 
#     page.goto(BASE_URL)
#     page.locator("#cookiescript_reject").click()
#     cookie_bar = page.locator(f"div#{'cookiescript_injected'}")
#     expect(cookie_bar).not_to_be_visible()

def accept_cookies_if_present(page: Page):
    """Klikne na tlačítko pro odmítnutí nebo přijetí cookies, pokud je zobrazeno."""
    cookies_button = page.get_by_role("button", name="Souhlasím jen s nezbytnými")
    if cookies_button.count() == 1:
        cookies_button.click() # cookies accept

def test_title_exists(page: Page): 
    page.goto(BASE_URL)
    expect(page).to_have_title("Kurzy programování a dalších IT technologií | ENGETO")

def test_button_terminy_visible(page: Page): 
    page.goto(BASE_URL)
    accept_cookies_if_present(page)

    expect(page.get_by_role("link", name="Kurzy", exact=True)).to_be_visible()
    page.get_by_role("link", name="Kurzy", exact=True).click()       
    expect(page.get_by_role("link", name="Zobrazit termíny kurzů")).to_be_visible()    
    page.get_by_role("link", name="Zobrazit termíny kurzů").click()
    

    expect(page).to_have_title("Termíny kurzů programování | ENGETO")
    expect(page).to_have_url(re.compile(".*terminy"))
   

def test_course_choise(page: Page):
    page.goto("https://engeto.cz/terminy/")
    accept_cookies_if_present(page)
    page.get_by_role("checkbox", name="Python Python").check()
    page.get_by_role("checkbox", name="Datová analýza Datová analýza").check()
    page.get_by_role("checkbox", name="Dlouhodobé (3–6 měsíců)").check()    
    
    kurzy = page.locator("text=Datový analytik s Pythonem")
    count = kurzy.count()
    assert count > 0, "Nenašel se žádný kurz s názvem 'Datový analytik s Pythonem'"    

    datum_element = page.locator("bold.has-text-lg-semibold-font-size").nth(10)
    expect(datum_element).to_have_text(re.compile(r"Od \d{1,2}\. [^\d\s]+")) # regular expression pro libovolné datum, měsíc s diakritikou
    #expect(page).to_have_url(re.compile(".*terminy")) 
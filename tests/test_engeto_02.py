import pytest
import re
from playwright.sync_api import sync_playwright, Page, expect

BASE_URL = "https://engeto.cz/"

def test_click_cookies_reject(page: Page):
    """Testing cookies on the active page in case they are reactivated.""" 
    page.goto(BASE_URL)
    page.locator("#cookiescript_reject").click()
    cookie_bar = page.locator(f"div#{'cookiescript_injected'}")
    expect(cookie_bar).not_to_be_visible()

def test_title_exists(page: Page): 
    page.goto(BASE_URL)
    expect(page).to_have_title("Kurzy programování a dalších IT technologií | ENGETO")

def test_button_terminy_visible(page: Page): 
    page.goto(BASE_URL)

    cookies_button = page.get_by_role("button", name="Souhlasím jen s nezbytnými")
    if cookies_button.count() == 1:
        cookies_button.click() # cookies accept
              
    expect(page.get_by_role("link", name="Termíny")).to_be_visible()
    page.get_by_role("link", name="Termíny").click()

    expect(page).to_have_title("Termíny kurzů programování | ENGETO")
    expect(page).to_have_url(re.compile(".*terminy"))
   

def test_course_choise(page: Page):
    page.goto("https://engeto.cz/terminy/")
    page.locator("#cookiescript_reject").click()
    page.get_by_role("checkbox", name="Python Python").check()
    page.get_by_role("checkbox", name="Datová analýza Datová analýza").check()
    page.get_by_role("checkbox", name="Dlouhodobé (3–6 měsíců)").check()    
    
    kurzy = page.locator("text=Datový analytik s Pythonem")
    count = kurzy.count()
    #print(f"Počet výskytů kurzu: {count}")
    #expect(kurzy.nth(0)).to_be_visible()
    assert count > 0, "Nenašel se žádný kurz s názvem 'Datový analytik s Pythonem'"
    

    datum_element = page.locator("bold.has-text-lg-semibold-font-size").nth(10)
    #expect(datum_element).to_have_text("Od 13. května")
    expect(datum_element).to_have_text("Od 20. května")

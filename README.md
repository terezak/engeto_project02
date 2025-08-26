# engeto_project02

## ZADÁNÍ
Napište tři automatizované testy pomocí frameworku Playwright. Vyberte si libovolnou webovou stránku, kterou chcete otestovat.

## INSTALACE

### Install packages
```bash
pip install playwright
pip install pytest
pip install pytest-playwright
```
### Install browsers

```bash
playwright install
```

### Run tests 
```bash
pytest
```
### Others
```bash
--headed
--slowmo 1000

pytest test_engeto_02.py --headed --slowmo 1000
```

-------------------------------------------------------

#### Page

page: Page – standard fixture provided by pytest-playwright

includes:

- sync_playwright()

- browser.launch()

- browser.close()

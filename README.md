# Install packages
pip install playwright
pip install pytest
pip install pytest-playwright

# Install browsers
playwright install

# Run tests 
pytest

# Others
--headed
--slowmo 1000

pytest test_engeto_02.py --headed --slowmo 1000

-------------------------------------------------------

# Page

page: Page – standard fixture provided by pytest-playwright

includes:
    sync_playwright()
    browser.launch()
    browser.close()
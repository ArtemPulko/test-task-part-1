from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36')
    service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service, options=options)
    chrome_browser.maximize_window()
    return chrome_browser


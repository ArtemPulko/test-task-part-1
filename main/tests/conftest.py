from pathlib import Path

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

@pytest.fixture(scope='session')
def driver():
    options = Options()
    #options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36')
    options.add_argument("--window-size=1680,1050")
    options.add_argument('--headless')
    project_root = Path(__file__).parents[2]
    driver_file = project_root / 'drivers' / 'chromedriver.exe'
    service = Service(executable_path= str(driver_file))
    chrome_browser = webdriver.Chrome(service = service, options = options)
    #chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()
@pytest.fixture
def authorization_cookies_path():
    project_root = Path(__file__).parents[2]
    cookies_file = project_root / 'resources' / 'cookies' / 'cookies.json'
    return cookies_file


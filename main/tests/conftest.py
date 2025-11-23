from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from drivers import get_chromedriver_path
from selenium import webdriver
from pathlib import Path
import pytest



@pytest.fixture(autouse=True, scope='session')
def driver():
    options = Options()
    options.add_argument("--window-size=1680,1050")
    options.add_argument('--headless')
    service = Service(executable_path= str(get_chromedriver_path(Path(__file__))))
    chrome_browser = webdriver.Chrome(service = service, options = options)
    yield chrome_browser
    chrome_browser.quit()

@pytest.fixture
def authorization_cookies_path():
    project_root = Path(__file__).parents[2]
    cookies_file = project_root / 'resources' / 'cookies' / 'cookies.json'
    return cookies_file


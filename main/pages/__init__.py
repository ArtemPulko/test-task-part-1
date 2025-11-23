from .onliner_phone_page import OnlinerMobilePhonePage
from .onliner_catalog_page import OnlinerCatalogPage
from .onliner_compare_page import ComparePage
from .onliner_page import OnlinerPage
import json


def authorization(driver, path: str):
    """
    Загрузка куков с заранее авторизованным пользователем.
    :param driver: Сетевой драйвер Chrome.
    :param path: Путь к кукам для авторизации
    """
    driver.delete_all_cookies()
    with open(path, 'r') as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

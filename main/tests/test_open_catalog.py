from main.pages import OnlinerCatalogPage, authorization
from main.pages import OnlinerPage
import pytest


@pytest.mark.run(order=1)
def test_mobile_phone_btn(driver, authorization_cookies_path):
    """
    Открыть категорию "Мобильные телефоны".
    Убедиться, что она открыта.
    :param authorization_cookies_path: Путь к кукам для авторизации
    """
    onliner_page = OnlinerPage(driver)
    # Открываю онлайнер
    onliner_page.open(onliner_page.url)
    # Перехожу в каталог телефонов
    onliner_page.mobile_phone_catalog.click()
    catalog_page = OnlinerCatalogPage(driver)
    authorization(driver, authorization_cookies_path)
    # Проверяю переход в каталог мобильных телефонов
    assert catalog_page.is_loaded, "Страница не загружена"

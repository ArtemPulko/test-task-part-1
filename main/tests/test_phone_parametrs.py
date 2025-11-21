from main.pages.onliner_phone_page import OnlinerMobilePhonePage
from main.pages.onliner_catalog_page import OnlinerMobilePage
from main.products.MobilePhone import MobilePhone
import pytest

@pytest.mark.run(order=4)
@pytest.mark.parametrize('phone_index', [(1,2,10)])
def test_phons_equals(driver, phone_index, authorization_cookies_path):
    """
    Перейти на любой из выбранных телефонов.
    Проверить, совпадают ли параметры с предыдущей страницей
    (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
    :param driver: Сетевой драйвер Chrome.
    :param phone_index: Содержит в себе
        phone_index: номер телефона по списку из тех что выбран для сравнения (в соответствии с условием может быть 1 или 2)
        phone_count: количество искомых телефонов (по условию - 2)
        search_range: диапазон поиска первых телефонов (по условию - 10).
    :param authorization_cookies_path: Путь к кукам для сравнения
    """
    catalog_page = OnlinerMobilePage(driver)
    phone_index, phone_count, search_range = phone_index
    phone_from_catalog = catalog_page.extract_from_characteristics(phone_index)
    catalog_page.open_phone_link(phone_index).click()
    phone_params_page = OnlinerMobilePhonePage(driver)
    phone_from_prod_info = phone_params_page.extract_from_characteristics_extended
    #Перейти на любой из выбранных телефонов и проверить, совпадают ли параметры с предыдущей страницей
    assert MobilePhone.is_equals(phone_from_catalog, phone_from_prod_info), 'Параметры телефонов не совпадают'


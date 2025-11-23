from main.pages import OnlinerMobilePhonePage
from main.pages import OnlinerCatalogPage
from main.products import MobilePhone
import pytest

@pytest.mark.run(order=4)
@pytest.mark.parametrize('phone_index', [1])
def test_phons_equals(driver, phone_index, authorization_cookies_path):
    """
    Перейти на любой из выбранных телефонов.
    Проверить, совпадают ли параметры с предыдущей страницей
    (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
    :param driver: Сетевой драйвер Chrome.
    :param phone_index: Содержит в себе
        phone_index: номер телефона по списку из тех что выбран для сравнения (в соответствии с условием может быть 1 или 2)
    :param authorization_cookies_path: Путь к кукам для сравнения
    """
    catalog_page = OnlinerCatalogPage(driver)
    phone_index = phone_index
    # Считывание характеристик телефона их краткого описания в каталоге
    phone_from_catalog = catalog_page.extract_from_characteristics(phone_index, True)
    # Перехожу в подробное описание телефона
    catalog_page.phone_link(phone_index).click()
    phone_params_page = OnlinerMobilePhonePage(driver)
    # Считывание характеристик телефона их подробного описания
    phone_from_prod_info = phone_params_page.extract_from_characteristics_extended
    # Перейти на любой из выбранных телефонов и проверить, совпадают ли параметры с предыдущей страницей
    assert MobilePhone.is_equals(phone_from_catalog, phone_from_prod_info), 'Параметры телефонов не совпадают'


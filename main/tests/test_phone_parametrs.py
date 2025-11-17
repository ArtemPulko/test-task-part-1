from main.pages.onliner_phone_page import OnlinerMobilePhonePage
from main.pages.onliner_catalog_page import OnlinerMobilePage
from selenium.webdriver import ActionChains, Keys
import pytest

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
    catalog_page.open()
    # Авторизация на сайте, необходима чтобы избавится от постоянно всплывающих окон
    catalog_page.authorization(driver, authorization_cookies_path)
    catalog_page.accept_city_btn.click()
    phone_index, phone_count, search_range = phone_index
    # Выбираю 2 случайных телефона из 10
    catalog_page.choice_telephone(driver, phone_count, search_range)
    actions = ActionChains(driver)
    #Листаю страницу до выбранного телефона (в противном случае информация не считывается)
    actions.move_to_element(catalog_page.selected_phone(phone_index)).perform()
    actions.key_down(Keys.PAGE_DOWN).perform()
    #Считываю параметры из описания телефона в каталоге
    phone_from_catalog = catalog_page.get_phone_params(phone_index)
    driver.implicitly_wait(5)
    #Перехожу на страницу подробного описания телефона
    catalog_page.get_phone(phone_index).click()
    phone_params_page = OnlinerMobilePhonePage(driver)
    #Считываю необходимые данные
    phone = phone_params_page.get_phone_params()
    #Перейти на любой из выбранных телефонов и проверить, совпадают ли параметры с предыдущей страницей
    assert phone_params_page.phons_param_is_equal(phone_from_catalog, phone), "Параметры телефонов не совпадают"


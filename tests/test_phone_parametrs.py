from pages.onliner_phone_page import OnlinerMobilePhonePage
from pages.onliner_catalog_page import OnlinerMobilePage
from selenium.webdriver import ActionChains, Keys
import pytest

@pytest.mark.parametrize('phone_index', [1])
def test_phons_equals(driver,phone_index, compare_cookies_path):
    """
    Перейти на любой из выбранных телефонов.
    Проверить, совпадают ли параметры с предыдущей страницей
    (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
    :param driver: Сетевой драйвер Chrome
    :param phone_index: номер телефона по списку из тех что выбран для сравнения (в соответствии с условием может быть 1 или 2)
    :param compare_cookies_path: Путь к кукам для сравнения
    """
    catalog_page = OnlinerMobilePage(driver)
    catalog_page.open()
    #По условию телефоны должны соответствовать выбранным из теста: test_select_phones
    #Поэтому загружаю куки с заранее подготовленными телефонами для обеспечения независимости тестов друг от друга
    #Тест может не сработает если onliner перемешает телефоны в каталоге
    catalog_page.set_compare(driver, compare_cookies_path)
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


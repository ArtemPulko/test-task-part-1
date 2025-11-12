from main.pages.onliner_phone_page import OnlinerMobilePhonePage
from main.pages.onliner_catalog_page import OnlinerMobilePage
from main.pages.onliner_compare_page import ComparePage
import pytest
import time

@pytest.mark.parametrize('phone_count', [2])
def test_compare_phons(driver, phone_count, compare_cookies_path):
    """
    Нажать на ссылку сравнения. Убедиться, что два телефона содержат правильную информацию
    (описанную в предыдущем шаге) и не совпадают друг с другом.
    :param driver: Сетевой драйвер Chrome
    :param phone_count: Количество телефонов в сравнении (по условию - 2)
    :param compare_cookies_path: Путь к кукам для сравнения
    :return:
    """
    catalog_page = OnlinerMobilePage(driver)
    catalog_page.open()
    #По условию телефоны должны соответствовать выбранным из теста: test_select_phones
    #Поэтому загружаю куки с заранее подготовленными телефонами для обеспечения независимости тестов друг от друга
    #Тест может не сработает если onliner перемешает телефоны в каталоге
    catalog_page.set_compare(driver, compare_cookies_path)
    phone_page = OnlinerMobilePhonePage(driver)
    time.sleep(15)
    #Перехожу в сравнение через каталог, потому что onliner создает для каждых телефонов разные ссылки
    catalog_page.comparison_link.click()
    compare_page = ComparePage(driver)
    #Начинаю перебирать телефоны
    for phone_index in range(1, phone_count + 1):
        #Создаю словарь с характеристиками телефона из сравнения
        param_from_compare = compare_page.get_phone_params(phone_index)
        #Перехожу на страницу с описанием телефона
        compare_page.open_phone_link(phone_index).click()
        # Создаю словарь с характеристиками этого же телефона из его описания
        param_from_product = phone_page.get_phone_params()
        #Убеждаюсь, что два телефона содержат правильную информацию.
        #Использую метод сравнивания характеристик
        if phone_page.phons_param_is_equal(param_from_product, param_from_compare):
            #Возвращаюсь в сравнение, чтобы проверить другой телефон
            phone_page.compare_link().click()
        else: assert False, "Данные телефонов не совпадают"
    #Проверяю не совпадают ли телефоны друг с другом.
    assert not compare_page.phons_name(1) == compare_page.phons_name(2), "В сравнении одинаковые телефоны"
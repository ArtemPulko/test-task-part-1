from main.pages.onliner_phone_page import OnlinerMobilePhonePage
from main.pages.onliner_compare_page import ComparePage
import pytest

from main.products.MobilePhone import MobilePhone

@pytest.mark.run(order=5)
@pytest.mark.parametrize('phone', [(2, 10)])
def test_compare_phons(driver, phone, authorization_cookies_path):
    """
    Нажать на ссылку сравнения. Убедиться, что два телефона содержат правильную информацию
    (описанную в предыдущем шаге) и не совпадают друг с другом.
    :param driver: Сетевой драйвер Chrome.
    :param phone: Содержит в себе:
        phone_count: количество искомых телефонов (по условию - 2)
        search_range: диапазон поиска первых телефонов (по условию - 10).
    :param authorization_cookies_path: Путь к кукам для сравнения
    :return:
    """
    phone_count, search_range = phone
    phone_page = OnlinerMobilePhonePage(driver)
    compare_page = ComparePage(driver)
    #Перехожу в сравнение телефонов
    phone_page.compare_link.click()
    compare_phone1, compare_phone2 = compare_page.extract_from_compare_characteristic
    phons = []
    for phone_index in range(phone_count):
        compare_page.get_phone_link(phone_index + 1).click()
        phons.append(phone_page.extract_from_characteristics_extended)
        phone_page.compare_link.click()
    assert (MobilePhone.is_equals(compare_phone1, phons[0])
            and MobilePhone.is_equals(compare_phone2, phons[1])), "Телефоны содержат не правильную информацию"



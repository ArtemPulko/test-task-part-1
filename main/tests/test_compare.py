from main.pages import OnlinerMobilePhonePage
from main.products import MobilePhone
from main.pages import ComparePage
import pytest

@pytest.mark.run(order=5)
@pytest.mark.parametrize('phone', [(2, [])])
def test_compare_phons(driver, phone):
    """
    Нажать на ссылку сравнения. Убедиться, что два телефона содержат правильную информацию
    (описанную в предыдущем шаге) и не совпадают друг с другом.
    :param driver: Сетевой драйвер Chrome.
    :param phone: Содержит в себе:
        phone_count: количество искомых телефонов (по условию - 2)
        phons: заготовка списка для телефонов
    :return:
    """
    phone_count, phons = phone
    phone_page = OnlinerMobilePhonePage(driver)
    compare_page = ComparePage(driver)
    # Перехожу в сравнение телефонов
    phone_page.compare_link.click()
    # Получаю данные о телефонах из таблицы сравнения
    compare_phone1, compare_phone2 = compare_page.extract_from_compare_characteristic
    # Получаю данные о телефонах из их описания
    for phone_index in range(phone_count):
        compare_page.get_phone_link(phone_index + 1).click()
        phons.append(phone_page.extract_from_characteristics_extended)
        phone_page.compare_link.click()
    # Сравниваю характеристики из сравнения и описания для первого телефона
    assert MobilePhone.is_equals(compare_phone1, phons[0]), "Первый телефон содержит неправильную информацию"
    # Сравниваю характеристики из сравнения и описания для второго телефона
    assert MobilePhone.is_equals(compare_phone2, phons[1]), "Второй телефон содержит неправильную информацию"
    # Проверяю чтобы телефоны не были одинаковы
    assert compare_page.get_phone_name(1) != compare_page.get_phone_name(2), "В сравнении два одинаковых телефона"



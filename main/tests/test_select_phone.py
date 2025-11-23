from main.pages import OnlinerCatalogPage
from main.products import MobilePhone
import random
import pytest

@pytest.mark.run(order=2)
@pytest.mark.parametrize('search',[(2, 10)])
def test_select_phones(driver, search):
    """
    Найти два любых телефона из первых 10 и добавить их для сравнения.
    Проверить, что ссылка для сравнения существует и флажки установлены.
    :param driver: Сетевой драйвер Chrome.
    :param search: Включает в себя следующее
        phone_count: количество искомых телефонов (по условию - 2)
        search_range: диапазон поиска первых телефонов (по условию - 10)
    """
    catalog_page = OnlinerCatalogPage(driver)
    #Закрываю всплывшее окно
    catalog_page.accept_city_btn.click()
    phone_count, search_range = search
    #Подгружаю 7-30 телефоны
    catalog_page.load_all_phons()
    for i in range(phone_count):
        catalog_page.phone_check_box(random.randint(1, search_range - i)).click()
    #Проверить, что ссылка для сравнения существует и флажки установлены
    assert catalog_page.comparison_link.is_displayed(), "Ссылка на сравнение не найдена"
    assert catalog_page.flags_in_place(phone_count), "Флажки не установлены"

@pytest.mark.run(order=3)
@pytest.mark.parametrize('params',[(2, [])])
def test_price_screen_range(driver, params):
    """
    Установить параметры поиска: цена (минимальная и максимальная),
    размер экрана (минимальный и максимальный) - соответствующие минимальным и максимальным параметрам выбранных телефонов.
    Убедиться, что выбранные телефоны по-прежнему отображаются и флажки установлены.
    :param driver: Сетевой драйвер Chrome.
    :param params: Включает в себя следующее
        phone_count: Количество выбранных телефонов (как по условию - 2)
        price_list: Пустой список, заготовка под цены телефонов
    """
    catalog_page = OnlinerCatalogPage(driver)
    phone_count, phone_list = params
    # Считываю информацию о телефонах из описания в каталоге
    for i in range(1, phone_count + 1):
        phone_list.append(catalog_page.extract_from_characteristics(i, False))
    # Ввод минимальной и максимальной цены
    catalog_page.enter_min_max_price(MobilePhone.min_max_price(phone_list))
    # Ввод минимального и максимального размера экрана
    catalog_page.enter_min_max_diagonal(MobilePhone.min_max_diagonal(phone_list))
    # Убедиться, что выбранные телефоны по-прежнему отображаются и флажки установлены.
    assert catalog_page.flags_in_place(phone_count), "Выбранные телефоны не отображаются"

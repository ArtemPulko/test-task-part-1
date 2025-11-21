from main.pages.onliner_catalog_page import OnlinerMobilePage
from main.products.MobilePhone import MobilePhone
from selenium.webdriver.common.by import By
from selenium.webdriver import  Keys
import random
import pytest

@pytest.mark.run(order=2)
@pytest.mark.parametrize('search',[(2, 10)])
def test_select_phones(driver, search, authorization_cookies_path):
    """
    Найти два любых телефона из первых 10 и добавить их для сравнения.
    Проверить, что ссылка для сравнения существует и флажки установлены.
    :param driver: Сетевой драйвер Chrome.
    :param search: Включает в себя следующее
        phone_count: количество искомых телефонов (по условию - 2)
        search_range: диапазон поиска первых телефонов (по условию - 10)
    :param authorization_cookies_path: Путь к кукам для авторизации
    """
    catalog_page = OnlinerMobilePage(driver)
    #Авторизация на сайте, необходима чтобы избавится от постоянно всплывающих окон
    catalog_page.authorization(driver, authorization_cookies_path)
    #Закрываю еще одно всплывшее окно
    catalog_page.accept_city_btn.click()
    phone_count, search_range = search
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)#  !!!!!!!
    phon_index = random.sample(range(1, search_range + 1), phone_count)
    for i in range(phone_count):
        catalog_page.phone_check_box(phon_index[i]).click()
    #Проверить, что ссылка для сравнения существует и флажки установлены
    assert catalog_page.comparison_link.is_displayed() and catalog_page.flags_in_place(phone_count), "Ссылка на сравнение не найдена или флажки не установлены"

@pytest.mark.run(order=3)
@pytest.mark.parametrize('params',[(10, 2, [],[])])
def test_price_screen_range(driver, params, authorization_cookies_path):
    """
    Установить параметры поиска: цена (минимальная и максимальная),
    размер экрана (минимальный и максимальный) - соответствующие минимальным и максимальным параметрам выбранных телефонов.
    Убедиться, что выбранные телефоны по-прежнему отображаются и флажки установлены.
    :param driver: Сетевой драйвер Chrome.
    :param params: Включает в себя следующее
        first_phons_of: Первые 10 телефонов
        phone_count: Количество выбранных телефонов (как по условию - 2)
        price_list: Пустой список, заготовка под цены телефонов
        screen_size Пустой список, заготовка под размеры экранов
    :param authorization_cookies_path: Путь к кукам для авторизации
    """
    catalog_page = OnlinerMobilePage(driver)
    first_phons_of, phone_count, phone_list, screen_size = params
    for i in range(1, phone_count + 1):
        phone_list.append(catalog_page.extract_from_characteristics(i))
    catalog_page.enter_min_max_price(MobilePhone.min_max_price(phone_list))
    catalog_page.enter_min_max_diagonal(MobilePhone.min_max_diagonal(phone_list))
    #Убедиться, что выбранные телефоны по-прежнему отображаются и флажки установлены.
    assert catalog_page.flags_in_place(phone_count), "Флажки не установлены"

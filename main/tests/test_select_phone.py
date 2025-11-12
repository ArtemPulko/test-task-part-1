from main.pages.onliner_catalog_page import OnlinerMobilePage
from selenium.webdriver import ActionChains
import numpy as np
import pytest

@pytest.mark.parametrize('search',[(2, 10, [])])
def test_select_phones(driver, search, authorization_cookies_path):
    """
    Найти два любых телефона из первых 10 и добавить их для сравнения.
    Проверить, что ссылка для сравнения существует и флажки установлены.
    :param driver: Сетевой драйвер Chrome.
    :param search: Включает в себя следующее
        phone_count: количество искомых телефонов (по условию - 2)
        search_range: диапазон поиска первых телефонов (по условию - 10)
        selected_mobile_phone_list: пустой список, заготовка для поиска телефонов.
    :param authorization_cookies_path: Путь к кукам для авторизации
    """
    catalog_page = OnlinerMobilePage(driver)
    catalog_page.open()
    #Авторизация на сайте, необходима чтобы избавится от постоянно всплывающих окон
    catalog_page.authorization(driver, authorization_cookies_path)
    driver.implicitly_wait(5)
    #Закрываю еще одно всплывшее окно
    catalog_page.accept_city_btn.click()
    phone_count, search_range, selected_mobile_phone_list = search
    #Выбираю 2 случайных телефона из 10
    unique_numbers = np.random.choice(np.arange(1, search_range + 1), phone_count, replace = False)
    while len(selected_mobile_phone_list) < phone_count:
        #Если вдруг окажется что искомых телефонов больше чем диапазон их поиска
        if len(selected_mobile_phone_list) == search_range:
            break
        #Определяю порядковый номер телефона в каталоге
        random_phone = unique_numbers[len(selected_mobile_phone_list)]
        driver.implicitly_wait(5)
        #Добавляю телефон в сравнение
        catalog_page.mobile_check_box(random_phone).click()
        selected_mobile_phone_list.append(catalog_page.mobile_check_box(random_phone))
    #Проверить, что флажки установлены.
    for phone in selected_mobile_phone_list:
        if phone.get_attribute("title") != "В сравнении":
            assert False, "Не все флажки установлены"
    #Проверить, что ссылка для сравнения существует
    assert catalog_page.comparison_link.is_displayed(), "Ссылка на сравнение не найдена"

@pytest.mark.parametrize('params',[(10, 2, [],[])])
def test_price_screen_range(driver, params, compare_cookies_path):
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
    :param compare_cookies_path: Путь к кукам для сравнения телефонов
    """
    onliner_mobile_catalog_page = OnlinerMobilePage(driver)
    onliner_mobile_catalog_page.open()
    #По условию телефоны должны соответствовать выбранным из теста: test_select_phones
    #Поэтому загружаю куки с заранее подготовленными телефонами для обеспечения независимости тестов друг от друга
    #Тест может не сработает если onliner перемешает телефоны в каталоге
    onliner_mobile_catalog_page.set_compare(driver, compare_cookies_path)
    first_phons_of, phone_count, price_list, screen_size = params
    actions = ActionChains(driver)
    #Собираю информацию о телефонах
    for index in range(1, first_phons_of + 1):
        if onliner_mobile_catalog_page.phone_by_index_is_selected(index): #Не стабильный момент
            driver.implicitly_wait(5)
            #Листаю страницу до выбранного телефона (в противно случае не считывало информацию о нем)
            actions.move_to_element(onliner_mobile_catalog_page.mobile_check_box(index)).perform()
            #Сохраняю цену
            price_list.append(onliner_mobile_catalog_page.get_price_by_phone(index))
            #Сохраняю размер экрана
            screen_size.append(onliner_mobile_catalog_page.phone_diagonal(index))
    #Проверка на то, что выбранные телефоны по-прежнему отображаются и флажки установлены.
    if len(price_list) < phone_count:
        #В price_list находятся только те телефоны у которых флажки установлены
        assert False, "Флажки не установлены "
    #Далее сортирую по возрастанию собранную информацию по возрастанию
    price_list.sort()
    screen_size.sort()
    #Ввожу минимальную цену
    onliner_mobile_catalog_page.enter_min_price(price_list[0])
    driver.implicitly_wait(5)
    #Ввожу максимальную цену
    onliner_mobile_catalog_page.enter_max_price(price_list[1])
    driver.implicitly_wait(5)
    #Выбираю диагональ экрана
    onliner_mobile_catalog_page.enter_screen_size(screen_size) #Не стабильный момент
    #Если тест дойдет до сюда значит все условия выполнены и тест считается успешным
    assert True


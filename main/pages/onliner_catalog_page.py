from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage
import time
import re

comparison_link = (By.XPATH, "(//a[@class='catalog-interaction__sub catalog-interaction__sub_main'])[1]")
accept_city = (By.XPATH, "//span[@class='button-style button-style_primary button-style_small-alter catalog-form__button']")
min_price = (By.XPATH, "(//input[@class='input-style input-style_primary input-style_small catalog-form__input catalog-form__input_width_full'])[1]")
max_price = (By.XPATH, "(//input[@class='input-style input-style_primary input-style_small catalog-form__input catalog-form__input_width_full'])[2]")
min_screen_size = (By.XPATH, "(//select[@class='input-style__real'])[5]")
max_screen_size = (By.XPATH, "(//select[@class='input-style__real'])[6]")
test_xpath= (By.XPATH, "//div[@class='input-style input-style_primary input-style_small input-style_arrow_bottom catalog-form__input catalog-form__input_width_full']")


class OnlinerMobilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """
        Метод для перехода на страницу по ссылке на каталог мобильных телефонов.
        """
        self.browser.get("https://catalog.onliner.by/mobile")

    def get_phone(self, phone_index):
        """
        Метод возвращающий ссылку для перехода в подробное описание телефона.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: WebElement ссылки подробного описания.
        """
        return self.find_by_xpath((By.XPATH, f"(//a[@class='catalog-form__link catalog-form__link_primary-additional catalog-form__link_base-additional catalog-form__link_font-weight_semibold catalog-form__link_nodecor'])[{phone_index}]"))

    def phone_os(self, phone_index):
        """
        Метод находит ос в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: Название операционной системы.
        """
        #Формула phone_index * 2 - 1 позволяет искать в описании только операционную систему
        locator = (By.XPATH, f"(//div[@class='catalog-form__parameter catalog-helpers_hide_tablet']//div[@class='catalog-form__description catalog-form__description_primary catalog-form__description_small-additional catalog-form__description_bullet catalog-form__description_condensed'][2])[{phone_index * 2 - 1}]")
        os_element = self.find_by_xpath(locator)
        return os_element.text

    def phone_screen_resolution(self, phone_index):
        """
        Метод находит разрешение экрана в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: Разрешение экрана телефона.
        """
        #Формула phone_index * 2 - 1 позволяет искать в описании только разрешение экрана
        locator = (By.XPATH, f"(//div[@class='catalog-form__parameter catalog-helpers_hide_tablet']//div[@class='catalog-form__description catalog-form__description_primary catalog-form__description_small-additional catalog-form__description_bullet catalog-form__description_condensed'][3])[{phone_index * 2 - 1}]")
        resolution_element = self.find_by_xpath(locator)
        screen = re.search(r'\((.+?)\)', resolution_element.text).group(1)
        return screen

    def phone_ram(self, phone_index):
        """
        Метод находит объем оперативной памяти в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: Объем оперативной памяти телефона.
        """
        # Формула phone_index * 2 - 1 позволяет искать в описании только объем оперативной памяти
        locator = (By.XPATH, f"(//div[@class='catalog-form__parameter catalog-helpers_hide_tablet']//div[@class='catalog-form__description catalog-form__description_primary catalog-form__description_small-additional catalog-form__description_bullet catalog-form__description_condensed'][5])[{phone_index * 2 - 1}]")
        ram_element = self.find_by_xpath(locator)
        ram = ram_element.text.replace('ОЗУ ', '')
        return ram

    def phone_diagonal(self, phone_index):
        """
         Метод находит размер экрана в описании телефона из каталога.
         :param phone_index: Порядковый номер телефона в каталоге.
         :return: Размер экрана телефона.
         """
        # Формула phone_index * 2 - 1 позволяет искать в описании только размер экрана
        locator = (By.XPATH, f"(//div[@class='catalog-form__offers-flex'][1]//div[@class='catalog-form__description catalog-form__description_primary catalog-form__description_small-additional catalog-form__description_bullet catalog-form__description_condensed'][3])[{phone_index * 2 - 1}]")
        screen_information = self.find_by_xpath(locator)
        diagonal = re.search(r' (.+?) ', screen_information.text).group(1)
        return diagonal

    def get_phone_params(self, phone_index):
        """
        Метод составляет словарь из свойств телефона
        (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: Словарь со свойствами телефона из каталога.
        """
        params = {}
        params["ОС"] = self.phone_os(phone_index)
        params["Размер экрана"] = self.phone_diagonal(phone_index)
        params["Разрешение экрана"] = self.phone_screen_resolution(phone_index)
        params["ОЗУ"] = self.phone_ram(phone_index)
        return params

    @property
    def accept_city_btn(self):
        """
        Свойство возвращающее кнопку для подтверждения города.
        :return: WebElement кнопки подтверждения города.
        """
        return self.find_by_xpath(accept_city)

    def mobile_check_box(self, index):
        """
        Метод определения "checkBox" для добавления в равнение.
        :param index: Порядковый номер телефона в каталоге.
        :return: WebElement условного checkBox.
        """
        #index * 2 - 1, формула точно определяет необходимый "checkBox" на странице для соответствующего телефона
        locator = (By.XPATH, f"(//div[@class='catalog-form__offers-part catalog-form__offers-part_image']//label[@class='catalog-form__checkbox-label'])[{index * 2 - 1}]")
        return self.find_by_xpath(locator)

    def phone_by_index_is_selected(self, index):
        """
        Метод для определения - выбран ли телефон в сравнение или нет.
        :param index: Порядковый номер телефона.
        :return: True если телефон добавлен в сравнение, иначе False.
        """
        if self.mobile_check_box(index).get_attribute("title") == "В сравнении": return True
        else: return False

    def selected_phone(self, phone_index):
        """
        Метод возвращающий телефон, который добавлен в сравнение.
        :param phone_index: Номер телефона по списку из тех, что в сравнении.
        :return: Web Element часть условного checkBox.
        """
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]")
        return self.find_by_xpath(locator)

    @property
    def comparison_link(self):
        """
        Свойство возвращающее ссылку на сравнение выбранных телефонов.
        :return: Web Element ссылки на сравнение.
        """
        return self.find_by_xpath(comparison_link)

    def get_price_by_phone(self, phone_index):
        """
        Метод возвращающий цену телефона с соответствующим порядковым номером.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: Цена в формате 0.00.
        """
        locator = (By.XPATH, f"(//div[@class='catalog-form__offers-flex'][1]//a[contains(@class,'catalog-form__link_huge-additional')]//span[2])[{phone_index}]")
        price_element = self.find_by_xpath(locator)
        price = price_element.text.split(' ')[0]
        return price

    @property
    def min_price_input(self):
        """
        Свойство находит input минимальной цены.
        :return: WebElement для ввода минимальной цены.
        """
        return self.find_by_xpath(min_price)

    @property
    def max_price_input(self):
        """
        Свойство находит input максимальной цены.
        :return: WebElement для ввода максимальной цены.
        """
        return self.find_by_xpath(max_price)

    def enter_min_price(self, price):
        """
        Метод посимвольно вводит цену в input минимальной цены.
        :param price: Цена в формате 0.00.
        """
        price_input = self.min_price_input
        for number in price.split(',')[0]:
            price_input.send_keys(int(number))
        price_input.send_keys('.')
        for number in price.split(',')[1]:
            price_input.send_keys(int(number))

    def enter_max_price(self, price):
        """
        Метод посимвольно вводит цену в input максимальной цены.
        :param price: Цена в формате 0.00.
        """
        price_input = self.max_price_input
        for number in price.split(',')[0]:
            price_input.send_keys(int(number))
        price_input.send_keys('.')
        for number in price.split(',')[1]:
            price_input.send_keys(int(number))

    @property
    def min_screen_size_selector(self):
        """
        Свойство находит select минимального размера экрана.
        :return: WebElement для выбора минимальной диагонали.
        """
        return self.find_by_xpath(min_screen_size)

    @property
    def max_screen_size_selector(self):
        """
        Свойство находит select максимального размера экрана.
        :return: WebElement для выбора максимального диагонали.
        """
        return self.find_by_xpath(max_screen_size)

    def enter_screen_size(self, screen_size):
        """
        Метод выбирает минимальную и максимальную диагональ экрана.
        :param screen_size: Список диагоналей, от меньшей к большей.
        """
        #Нахожу необходимые select
        min_select = self.min_screen_size_selector
        max_selector = self.max_screen_size_selector
        actions = ActionChains(self.browser)
        #Последующие 4 строки прокручивают страницу до необходимых select
        actions.click(min_select).perform()
        time.sleep(1)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        #Выбираю минимальный размер экрана
        time.sleep(1)
        min_select.click()
        Select(min_select).select_by_visible_text(screen_size[0])
        #Выбираю максимальный размер экрана
        time.sleep(1)
        max_selector.click()
        Select(max_selector).select_by_visible_text(screen_size[1])



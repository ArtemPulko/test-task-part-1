from main.pages.locators.catalog_locators import CatalogLocator as CL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from main.products import PhoneCharacteristic
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage
from main.products import MobilePhone
from selenium.webdriver import Keys
from decimal import Decimal
import json
import re

class OnlinerCatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def phone_screen_resolution(self, phone_index: int) -> str:
        """
        Метод находит разрешение экрана в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Разрешение экрана телефона.
        """
        resolution_element = self.find_by_xpath(CL.xpath_screen_resolution.upgrade(phone_index))
        screen = re.search(r'\((.+?)\)', resolution_element.text).group(1)
        return screen

    def phone_diagonal(self, phone_index: int) -> Decimal:
        """
         Метод находит размер экрана в описании телефона из каталога.
         :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
         :return: Размер экрана телефона.
         """
        screen_information = self.find_by_xpath(CL.xpath_diagonal.upgrade(phone_index))
        diagonal = re.search(r' (.+?) ', screen_information.text).group(1)
        diagonal = diagonal.replace('"', '')
        return Decimal(diagonal)

    def phone_price(self, phone_index: int) -> Decimal:
        """
        Метод находит цену телефона в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Цена в формате 0.00.
        """
        price_element = self.find_by_xpath(CL.xpath_price.upgrade(phone_index))
        price = price_element.text.split(' ')[0]
        price = price.replace(',','.')
        return Decimal(price)

    def phone_ram(self, phone_index: int) -> int:
        """
        Метод находит объем оперативной памяти в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Объем оперативной памяти телефона.
        """
        ram_element = self.find_by_xpath(CL.xpath_ram.upgrade(phone_index))
        ram = re.search(r' (.+?) ', ram_element.text).group(1)
        return int(ram)

    def phone_os(self, phone_index: int) -> str:
        """
        Метод находит ос в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Название операционной системы.
        """
        os_element = self.find_by_xpath(CL.xpath_os.upgrade(phone_index))
        return os_element.text

    def extract_from_characteristics(self, phone_index: int, is_full: bool) -> MobilePhone:
        """
        Метод создает телефон с параметрами взятыми со страницы каталога
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :param is_full: Режим работы метода. Если True, то метод считает всю необходимую информацию, иначе только цену и диагональ экрана.
        :return: Объект MobilePhone с характеристиками
        """
        phone = MobilePhone()
        phone.add_characteristic(PhoneCharacteristic.price.value, self.phone_price(phone_index))
        phone.add_characteristic(PhoneCharacteristic.diagonal.value, self.phone_diagonal(phone_index))
        if is_full:
            phone.add_characteristic(PhoneCharacteristic.os.value, self.phone_os(phone_index))
            phone.add_characteristic(PhoneCharacteristic.ram.value, self.phone_ram(phone_index))
            phone.add_characteristic(PhoneCharacteristic.screen_resolution.value, self.phone_screen_resolution(phone_index))
        return phone

    def phone_check_box(self, phone_index: int) -> WebElement:
        """
        Метод определения "checkBox" для добавления в сравнение.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: WebElement условного checkBox.
        """
        return self.find_by_xpath_clickable_elem(CL.xpath_add_phone.upgrade(phone_index))

    def selected_phone(self, phone_index: int) -> WebElement:
        """
        Метод возвращающий телефон, который добавлен в сравнение.
        :param phone_index: Номер телефона по списку из тех, что в сравнении.
        :return: WebElement часть условного checkBox.
        """
        return self.find_by_xpath(CL.xpath_selected_phone.upgrade(phone_index))

    def flags_in_place(self, phone_count: int) -> bool:
        """
        Метод для уточнения статуса флажков
        :param phone_count: Номер телефона по списку из тех, что в сравнении.
        :return: True, если флажки установлены, иначе False
        """
        for i in range(1, phone_count + 1):
            try:
                #Отличие между чек боксами только в атрибуте title
                if self.selected_phone(i).get_attribute('title') == 'В сравнении':
                    #Если количество чек боксов с "title == В сравнении" равно количеству искомых телефонов по условию...
                    if i == phone_count:
                        #Значит все флажки установлены
                        return True
                else: break
            except TimeoutException:
                return False
        return False

    def phone_link(self, phone_index: int) -> WebElement:
        """
        Метод возвращающий ссылку для перехода в подробное описание телефона.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: WebElement ссылки подробного описания.
        """
        #Ожидает пока обновится список телефонов в каталоге после добавления фильтров
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(CL.offers.value))
        return self.find_by_xpath_clickable_elem(CL.xpath_link2.upgrade(phone_index))

    @property
    def accept_city_btn(self) -> WebElement:
        """
        Свойство возвращающее кнопку для подтверждения города.
        :return: WebElement кнопки подтверждения города.
        """
        return self.find_by_xpath_clickable_elem(CL.accept_city.value)

    @property
    def comparison_link(self) -> WebElement:
        """
        Свойство возвращающее ссылку на сравнение выбранных телефонов.
        :return: Web Element ссылки на сравнение.
        """
        return self.find_by_xpath(CL.comparison_link.value)

    def enter_min_max_diagonal(self, min_max_diagonal: tuple[Decimal, Decimal]):
        """
        Метод для выбора минимальной и максимальной диагонали экрана в фильтре для поиска телефонов.
        :param min_max_diagonal: Картеж с минимальной и максимальной диагональю экран.
        """
        for i in range(1, len(min_max_diagonal) + 1):
            diagonal_select = self.find_by_xpath_presence_elem(CL.xpath_select_diagonal.upgrade(i))
            diagonal_str = str(min_max_diagonal[i - 1]) + '"'
            self.scroll_to_element(diagonal_select)
            diagonal_select.click()
            Select(diagonal_select).select_by_visible_text(diagonal_str)
            # Ожидает пока обновится список телефонов в каталоге после добавления фильтров
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(CL.offers.value))

    def enter_min_max_price(self, min_max_price: tuple[Decimal, Decimal]):
        """
        Метод для посимвольного ввода минимальной и максимальной цены в фильтре для поиска телефонов.
        :param min_max_price: Картеж с минимальной и максимальной ценой.
        """
        for i in range(1, len(min_max_price) + 1):
            CL.xpath_price_input.upgrade(i)
            price_input = self.find_by_xpath_clickable_elem(CL.xpath_price_input.upgrade(i))
            price_str = str(min_max_price[i - 1])
            for number in price_str:
                if number == '.' : price_input.send_keys('.')
                else: price_input.send_keys(number)
            # Ожидает пока обновится список телефонов в каталоге после добавления фильтров
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CL.offers.value))

    @property
    def is_loaded(self) -> bool:
      """
      Свойство для подтверждения перехода на страницу
      :return: True если элемент на странице отображается, иначе False
      """
      try:
          WebDriverWait(self.driver, 10).until(EC.url_to_be("https://catalog.onliner.by/mobile"))
          WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CL.catalog.value))
          return True
      except TimeoutException:
          return False

    def load_all_phons(self):
        """Метод для загрузки телефонов в каталоге."""
        #Onliner подгружает на страницу только первые шесть телефонов из-за этого другие некликабельны
        #Поэтому листаю страницу до самого низа, чтобы они подгрузились в каталог
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
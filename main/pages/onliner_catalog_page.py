from decimal import Decimal

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.pages.base_page import BasePage
import re

from main.products.MobilePhone import MobilePhone
from main.products.PhoneCharacteristic import PhoneCharacteristic

comparison_link = (By.XPATH, "(//a[@class='catalog-interaction__sub catalog-interaction__sub_main'])[1]")
accept_city = (By.XPATH, "//span[@class='button-style button-style_primary button-style_small-alter catalog-form__button']")
price_input_xpath = "(//input[@class='input-style input-style_primary input-style_small catalog-form__input catalog-form__input_width_full'])[input_index]"
select_diagonal_xpath = "((//div[@class='catalog-form__line catalog-form__line_condensed-other'])[16]//select[1])[select_index]"
test_xpath= (By.XPATH, "//div[@class='input-style input-style_primary input-style_small input-style_arrow_bottom catalog-form__input catalog-form__input_width_full']")
offers_locator = (By.XPATH, "//div[@class='catalog-form__offers catalog-form__offers_processing'][1]")

class OnlinerMobilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_phone(self, phone_index):
        """
        Метод возвращающий ссылку для перехода в подробное описание телефона.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: WebElement ссылки подробного описания.
        """
        return self.find_by_xpath((By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]/parent::div/parent::div//a[contains(@class,'catalog-form__link_base-additional')]"))

    def phone_os(self, phone_index):
        """
        Метод находит ос в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Название операционной системы.
        """
        #Формула phone_index * 2 - 1 позволяет искать в описании только операционную систему
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[2]")
        os_element = self.find_by_xpath(locator)
        return os_element.text

    def phone_screen_resolution(self, phone_index):
        """
        Метод находит разрешение экрана в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Разрешение экрана телефона.
        """
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[3]")
        resolution_element = self.find_by_xpath(locator)
        screen = re.search(r'\((.+?)\)', resolution_element.text).group(1)
        return screen

    def phone_ram(self, phone_index):
        """
        Метод находит объем оперативной памяти в описании телефона из каталога.
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Объем оперативной памяти телефона.
        """
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[5]")
        ram_element = self.find_by_xpath(locator)
        ram = re.search(r' (.+?) ', ram_element.text).group(1)
        return int(ram)

    def phone_diagonal(self, phone_index):
        """
         Метод находит размер экрана в описании телефона из каталога.
         :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
         :return: Размер экрана телефона.
         """
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[3]")
        screen_information = self.find_by_xpath(locator)
        diagonal = re.search(r' (.+?) ', screen_information.text).group(1)
        diagonal = diagonal.replace('"', '')
        return Decimal(diagonal)

    def phone_price(self, phone_index):
        """
        Метод возвращающий цену телефона с соответствующим порядковым номером.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: Цена в формате 0.00.
        """
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]/parent::div/parent::div[@class='catalog-form__offers-flex'][1]//a[contains(@class,'catalog-form__link_huge-additional')]//span[2][1]")
        price_element = self.find_by_xpath(locator)
        price = price_element.text.split(' ')[0]
        price = price.replace(',','.')
        return Decimal(price)

    def create_phone_with_characteristics(self, phone_index):
        """
        Метод создает телефон с параметрами взятыми со страницы каталога
        :param phone_index: Порядковый номер телефона в каталоге из добавленных к сравнению.
        :return: Объект MobilePhone с характеристиками
        """
        phone = MobilePhone()
        phone.add_characteristic(PhoneCharacteristic.os, self.phone_os(phone_index))
        phone.add_characteristic(PhoneCharacteristic.ram, self.phone_ram(phone_index))
        phone.add_characteristic(PhoneCharacteristic.price, self.phone_price(phone_index))
        phone.add_characteristic(PhoneCharacteristic.diagonal, self.phone_diagonal(phone_index))
        phone.add_characteristic(PhoneCharacteristic.screen_resolution, self.phone_screen_resolution(phone_index))
        return phone

    @property
    def accept_city_btn(self):
        """
        Свойство возвращающее кнопку для подтверждения города.
        :return: WebElement кнопки подтверждения города.
        """
        return self.find_by_xpath_clickable_elem(accept_city)

    def phone_check_box(self, phone_index):
        """
        Метод определения "checkBox" для добавления в равнение.
        :param phone_index: Порядковый номер телефона в каталоге.
        :return: WebElement условного checkBox.
        """
        self.driver.save_screenshot("element_to_be_clickable.png")
        locator = (By.XPATH, f"(//label[@title='К сравнению'])[{phone_index}]")
        return self.find_by_xpath_clickable_elem(locator)

    def selected_phone(self, phone_index):
        """
        Метод возвращающий телефон, который добавлен в сравнение.
        :param phone_index: Номер телефона по списку из тех, что в сравнении.
        :return: WebElement часть условного checkBox.
        """
        locator = (By.XPATH, f"(//label[@title='В сравнении'])[{phone_index}]")
        return self.find_by_xpath(locator)
    def flags_in_place(self, phone_count):
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

    @property
    def comparison_link(self):
        """
        Свойство возвращающее ссылку на сравнение выбранных телефонов.
        :return: Web Element ссылки на сравнение.
        """
        return self.find_by_xpath(comparison_link)

    def enter_min_max_price(self, min_max_price):
        for i in range(1, len(min_max_price) + 1):
            price_input = self.find_by_xpath_clickable_elem((By.XPATH, price_input_xpath.replace('input_index', str(i))))
            price_str = str(min_max_price[i - 1])
            for number in price_str:
                if number == '.' : price_input.send_keys('.')
                else: price_input.send_keys(int(number))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(offers_locator))

    def enter_min_max_diagonal(self, min_max_diagonal):
        for i in range(1, len(min_max_diagonal) + 1):
            diagonal_select = self.find_by_xpath_presence_elem((By.XPATH, select_diagonal_xpath.replace('select_index', str(i))))
            diagonal_str = str(min_max_diagonal[i - 1]) + '"'
            self.driver.execute_script("arguments[0].scrollIntoView();", diagonal_select)
            diagonal_select.click()
            Select(diagonal_select).select_by_visible_text(diagonal_str)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(offers_locator))
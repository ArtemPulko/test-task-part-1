from main.pages.locators.phone_info_locators import PhoneInfoLocators as PL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from main.products import PhoneCharacteristic
from selenium.common import TimeoutException
from main.pages.base_page import BasePage
from main.products import MobilePhone
from decimal import Decimal

class OnlinerMobilePhonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def extract_from_characteristics_extended(self) -> MobilePhone:
        """
        Свойство считывает информацию из таблицы характеристик и возвращает телефон с данной информацией
        :return: Телефон с характеристиками
        """
        phone = MobilePhone()
        row = 2
        while True:
            try:
                #Проверка на конец таблицы характеристик
                WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(PL.xpath_characteristic.upgrade(row)))
                #Считывание названия характеристики
                characteristic = self.find_by_xpath(PL.xpath_characteristic.upgrade(row)).text
                #Считывание значения характеристики
                value = self.find_by_xpath(PL.xpath_value.upgrade(row)).text
                if characteristic == PhoneCharacteristic.ram.value:
                    value = int(value.replace(' ГБ',''))
                if characteristic == PhoneCharacteristic.diagonal.value:
                    value = Decimal(value.replace('"', ''))
                phone.add_characteristic(characteristic, value)
                row += 1
            except TimeoutException:
                break
        return phone

    @property
    def compare_link(self) -> WebElement:
        """
        Свойство возвращающее ссылку на сравнение выбранных телефонов.
        :return: WebElement ссылки на сравнение.
        """
        return self.find_by_xpath_clickable_elem(PL.compare_link.value)
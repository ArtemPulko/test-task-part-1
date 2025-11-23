from main.pages.locators.in_compare_locators import CompareLocator as CL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from main.products import PhoneCharacteristic
from selenium.common import TimeoutException
from main.pages.base_page import BasePage
from main.products import MobilePhone
from decimal import Decimal

class ComparePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_phone_link(self, phone_index: int) -> WebElement:
        """
        Метод возвращающий ссылку на характеристики телефона.
        :param phone_index: Порядковый номер телефона в сравнении.
        :return: WebElement ссылки на телефон.
        """
        return self.find_by_xpath_clickable_elem(CL.phone_name_xpath.upgrade(phone_index))

    def get_phone_name(self, phone_index: int) -> str:
        """
        Метод возвращающий название телефона.
        :param phone_index: Порядковый номер телефона в сравнении.
        :return: Название телефона.
        """
        return self.find_by_xpath_clickable_elem(CL.phone_name_xpath.upgrade(phone_index)).text

    @property
    def extract_from_compare_characteristic(self) -> tuple[MobilePhone, MobilePhone]:
        """
        Свойство считывает информацию из таблицы характеристик и возвращает картеж из двух телефонов с данной информацией
        :return: Картеж из двух телефонов содержащих информацию из первой таблицы характеристик
        """
        phone1 = MobilePhone()
        phone2 = MobilePhone()
        row = 2
        while True:
            try:
                #Проверка на конец таблицы характеристик
                WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(CL.characteristic_xpath.upgrade(row)))
                #Считывание названия характеристики
                characteristic = self.find_by_xpath(CL.characteristic_xpath.upgrade(row)).text
                #Считывание значения характеристики первого телефона
                value1 = self.find_by_xpath(CL.value1_xpath.upgrade(row)).text
                #Считывание значения характеристики второго телефона
                value2 = self.find_by_xpath(CL.value2_xpath.upgrade(row)).text
                if characteristic == PhoneCharacteristic.ram.value:
                    value1 = int(value1.replace(' ГБ',''))
                    value2 = int(value2.replace(' ГБ',''))
                if characteristic == PhoneCharacteristic.diagonal.value:
                    value1 = Decimal(value1.replace('"', ''))
                    value2 = Decimal(value2.replace('"', ''))
                phone1.add_characteristic(characteristic, value1)
                phone2.add_characteristic(characteristic, value2)
                row += 1
            except TimeoutException:
                break
        return phone1, phone2
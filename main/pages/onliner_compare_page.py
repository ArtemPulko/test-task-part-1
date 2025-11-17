import re

from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage

class ComparePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def phone_os(self, phone_index):
        """
        Свойство находит и возвращает название операционной системы из таблицы характеристик телефона.
        :return: Название операционной системы.
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[1]//span[@class='product-table__wrapper'])[{row}]")).text == "Операционная система":
                return self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[{phone_index + 2}]//span[@class='product-table__wrapper'])[{row}]")).text
            else: row += 1

    def phone_screen(self, phone_index):
        """
        Свойство находит и возвращает разрешение экрана из таблицы характеристик телефона.
        :return: Значение разрешения экрана в формате - 1280х720
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[1]//span[@class='product-table__wrapper'])[{row}]")).text == "Разрешение экрана":
                return self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[{phone_index + 2}]//span[@class='product-table__wrapper'])[{row}]")).text
            else: row += 1

    def phone_diagonal(self, phone_index):
        """
        Свойство находит и возвращает размер экрана из таблицы характеристик телефона
        :return: Значение размера экрана в формате - 6.1"
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[1]//span[@class='product-table__wrapper'])[{row}]")).text == "Размер экрана":
                return self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[{phone_index + 2}]//span[@class='product-table__wrapper'])[{row}]")).text
            else: row += 1

    def phone_ram(self, phone_index):
        """
        Свойство находит и возвращает объем оперативной памяти из таблицы характеристик телефона
        :return: Значение объема оперативной памяти
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[1]//span[@class='product-table__wrapper'])[{row}]")).text == "Объем оперативной памяти":
                print(self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[{phone_index + 2}]//span[@class='product-table__wrapper'])[{row}]")).text)
                ram_str = self.find_by_xpath((By.XPATH, f"(//tbody[@class='product-table__group'][2]//tr[contains(@class,'product-table__row product-table__row_parameter')]//td[{phone_index + 2}]//span[@class='product-table__wrapper'])[{row}]")).text
                ram = ram_str.split('ГБ')[0].strip()
                return int(ram)
            else: row += 1

    def get_phone_params(self, phone_index):
        """
        Метод составляет словарь из свойств телефона
        (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
        :param phone_index: Порядковый номер телефона в сравнении.
        :return: Словарь со свойствами телефона из сравнения.
        """
        params = {}
        params["ОС"] = self.phone_os(phone_index)
        params["Размер экрана"] = self.phone_diagonal(phone_index)
        params["Разрешение экрана"] = self.phone_screen(phone_index)
        params["ОЗУ"] = self.phone_ram(phone_index)
        return params

    def open_phone_link(self, phone_index):
        """
        Метод возвращающий ссылку для перехода в подробное описание телефона.
        :param phone_index: Порядковый номер телефона в сравнении.
        :return: WebElement ссылки подробного описания.
        """
        locator = (By.XPATH, f"(//tr[@class='product-table__row product-table__row_header product-table__row_top']//span[@class='product-summary__caption'])[{phone_index}]")
        return self.find_by_xpath(locator)

    def phons_name(self, phone_index):
        """
        Метод возвращающий названия телефона.
        :param phone_index: Порядковый номер телефона в сравнении.
        :return: Название телефона.
        """
        phon_name_locator = (By.XPATH, f"(//span[@class='product-summary__caption'])[{phone_index}]")
        return self.find_by_xpath(phon_name_locator).text
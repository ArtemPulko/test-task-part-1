from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage

compare_link_locator = (By.XPATH, "//a[@class='catalog-interaction__sub catalog-interaction__sub_main']")


class OnlinerMobilePhonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def phone_os(self):
        """
        Свойство находит и возвращает название операционной системы из таблицы характеристик телефона.
        :return: Название операционной системы.
        """
        row = 1
        #Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]")).text == "Операционная система":
                return self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[2]")).text
            else: row += 1

    @property
    def phone_screen(self):
        """
        Свойство находит и возвращает разрешение экрана из таблицы характеристик телефона.
        :return: Значение разрешения экрана в формате - 1280х720
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]")).text == "Разрешение экрана":
                return self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[2]")).text
            else: row += 1

    @property
    def phone_diagonal(self):
        """
        Свойство находит и возвращает размер экрана из таблицы характеристик телефона
        :return: Значение размера экрана в формате - 6.1"
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]")).text == "Размер экрана":
                return self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[2]")).text
            else: row += 1

    @property
    def phone_ram(self):
        """
        Свойство находит и возвращает объем оперативной памяти из таблицы характеристик телефона
        :return: Значение объема оперативной памяти в формате - 8 ГБ
        """
        row = 1
        # Итерируюсь по таблице характеристик от первой строки до искомой
        while True:
            if self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]")).text == "Объем оперативной памяти":
                return self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[2]")).text
            else: row += 1

    def get_phone_params(self):
        """
        Метод составляет словарь из свойств телефона
        (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
        :return: Словарь со свойствами телефона из его подробного описания.
        """
        params = {}
        params["ОС"] = self.phone_os
        params["Размер экрана"] = self.phone_diagonal
        params["Разрешение экрана"] = self.phone_screen
        params["ОЗУ"] = self.phone_ram
        return params

    def compare_link(self):
        """
        Свойство возвращающее ссылку на сравнение выбранных телефонов.
        :return: WebElement ссылки на сравнение.
        """
        return self.find_by_xpath(compare_link_locator)

    def phons_param_is_equal(self, another_phon, phone):
        """
        Метод определяющий совпадение всех свойств обоих телефонов.
        :param another_phon: Словарь свойств телефона из каталога
        :param phone: Словарь свойств телефона из его подробного описания
        :return: True если свойства одинаковы, иначе False
        """
        for parameter in phone:
            if another_phon[parameter] != phone[parameter]:
                return False
        return True
from decimal import Decimal

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.pages.base_page import BasePage
from main.products.MobilePhone import MobilePhone
from main.products.PhoneCharacteristic import PhoneCharacteristic

phone_name_xpath = "(//a[@class='product-summary__figure']//span)[{PI}]"
compare_characteristic_xpath = '//tbody[5]//tr[contains(@class, "product-table__row")][{row}]/td[1]'
value1_characteristic_xpath = '//tbody[5]//tr[contains(@class, "product-table__row")][{row}]/td[3]'
value2_characteristic_xpath = '//tbody[5]//tr[contains(@class, "product-table__row")][{row}]/td[4]'

class ComparePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_phone_link(self, phone_index):
        """
        Метод возвращающий названия телефона.
        :param phone_index: Порядковый номер телефона в сравнении.
        :return: Название телефона.
        """
        return self.find_by_xpath_clickable_elem((By.XPATH, phone_name_xpath.replace('{PI}', str(phone_index))))

    @property
    def extract_from_compare_characteristic(self):
        phone1 = MobilePhone()
        phone2 = MobilePhone()
        row = 2
        while True:
            try:
                WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH,compare_characteristic_xpath.replace('{row}', str(row)))))
                characteristic = self.find_by_xpath((By.XPATH,compare_characteristic_xpath.replace('{row}', str(row)))).text
                value1 = self.find_by_xpath((By.XPATH,value1_characteristic_xpath.replace('{row}', str(row)))).text
                value2 = self.find_by_xpath((By.XPATH,value2_characteristic_xpath.replace('{row}', str(row)))).text
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
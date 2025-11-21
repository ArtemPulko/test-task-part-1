from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.products.PhoneCharacteristic import PhoneCharacteristic
from main.products.MobilePhone import MobilePhone
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage
from decimal import Decimal

compare_link_locator = (By.XPATH, "//a[@class='catalog-interaction__sub catalog-interaction__sub_main']")

class OnlinerMobilePhonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def extract_from_characteristics_extended(self):
        phone = MobilePhone()
        row = 2
        while True:
            try:
                WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]")))
                characteristic = self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]")).text
                value = self.find_by_xpath((By.XPATH, f"//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[2]")).text
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
    def compare_link(self):
        """
        Свойство возвращающее ссылку на сравнение выбранных телефонов.
        :return: WebElement ссылки на сравнение.
        """
        self.driver.save_screenshot("onliner_phone_page.png")
        return self.find_by_xpath_clickable_elem(compare_link_locator)
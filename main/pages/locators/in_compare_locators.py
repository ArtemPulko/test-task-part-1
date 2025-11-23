from selenium.webdriver.common.by import By
import enum

class CompareLocator(enum.Enum):
    # XPATH требующий обработки
    phone_name_xpath = "(//a[@class='product-summary__figure']//span)[{PI}]"
    characteristic_xpath = '//tbody[5]//tr[contains(@class, "product-table__row")][{PI}]/td[1]'
    value1_xpath = '//tbody[5]//tr[contains(@class, "product-table__row")][{PI}]/td[3]'
    value2_xpath = '//tbody[5]//tr[contains(@class, "product-table__row")][{PI}]/td[4]'

    def upgrade(self, index: int) -> tuple[str, str]:
        """
        Метод для дополнения xpath, с которым нужно итерироваться по вэб элементам
        :param index: порядковый номер элемента
        :return: Картеж вида (By.XPATH, xpath)
        """
        return By.XPATH, self.value.replace('{PI}', str(index))

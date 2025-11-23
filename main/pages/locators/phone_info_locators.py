from selenium.webdriver.common.by import By
import enum

class PhoneInfoLocators(enum.Enum):
    # XPATH требующий обработки
    xpath_characteristic = "//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[1]"
    xpath_value = "//table[@class='product-specs__table']/tbody[2]/tr[{row}]/td[2]"

    #XPATH локаторы
    compare_link = (By.XPATH, "//a[@class='catalog-interaction__sub catalog-interaction__sub_main']")

    def upgrade(self, index: int) -> tuple[str, str]:
        """
        Метод для дополнения xpath, с которым нужно итерироваться по вэб элементам
        :param index: порядковый номер элемента
        :return: Картеж вида (By.XPATH, xpath)
        """
        return By.XPATH, self.value.replace('{row}', str(index))
from selenium.webdriver.common.by import By
import enum

class CatalogLocator(enum.Enum):
    # XPATH требующий обработки
    xpath_price = "(//label[@title='В сравнении'])[{PI}]/parent::div/parent::div[@class='catalog-form__offers-flex'][1]//a[contains(@class,'catalog-form__link catalog-form__link_nodecor')]/span[contains(text(), 'р.')][1]"
    xpath_price_input = "(//input[@class='input-style input-style_primary input-style_small catalog-form__input catalog-form__input_width_full'])[{PI}]"
    xpath_screen_resolution = "(//label[@title='В сравнении'])[{PI}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[3]"
    xpath_diagonal = "(//label[@title='В сравнении'])[{PI}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[3]"
    xpath_ram = "(//label[@title='В сравнении'])[{PI}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[5]"
    xpath_os = "(//label[@title='В сравнении'])[{PI}]/parent::div/parent::div//div[contains(@class,'parameter-part_1')]/div[2]"
    xpath_select_diagonal = "((//div[@class='catalog-form__line catalog-form__line_condensed-other'])[16]//select[1])[{PI}]"
    xpath_link2 = "(//label[@title='В сравнении'])[{PI}]/parent::div/parent::div//h3"
    xpath_selected_phone = "(//label[@title='В сравнении'])[{PI}]"
    xpath_add_phone = "(//label[@title='К сравнению'])[{PI}]"
    # XPATH локаторы
    accept_city = (By.XPATH,"//span[@class='button-style button-style_primary button-style_small-alter catalog-form__button']")
    comparison_link = (By.XPATH, "(//a[@class='catalog-interaction__sub catalog-interaction__sub_main'])[1]")
    offers = (By.XPATH, "//div[@class='catalog-form__offers catalog-form__offers_processing'][1]")
    catalog = (By.XPATH, "//div[@class='catalog-form']")


    def upgrade(self, index: int) -> tuple[str, str]:
        """
        Метод для дополнения xpath, с которым нужно итерироваться по вэб элементам
        :param index: порядковый номер элемента
        :return: Картеж вида (By.XPATH, xpath)
        """
        return By.XPATH, self.value.replace('{PI}', str(index))

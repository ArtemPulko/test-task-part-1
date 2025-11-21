from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from main.pages.base_page import BasePage

mobilePhone_selector = (By.XPATH, '(//a[@class="project-navigation__link project-navigation__link_primary"])[1]')

class OnlinerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Метод для перехода на страницу по ссылке."""
        self.driver.get("https://www.onliner.by/")

    @property
    def mobile_phone_btn(self):
        """
        Свойство для поиска кнопки перехода в каталог.
        :return: WebElement кнопки перехода в каталог мобильных телефонов.
        """
        return self.find_by_xpath_clickable_elem(mobilePhone_selector)

    @property
    def cotalog_isLoaded(self):
        """
        Свойство проверяющее переход пользователя на необходимую страницу
        :return: True если переход успешный, иначе False
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.url_to_be("https://catalog.onliner.by/mobile"))
            return True
        except TimeoutException:
            return False


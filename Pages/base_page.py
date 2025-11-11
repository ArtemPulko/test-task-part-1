from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_by_xpath(self, locator):
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """
        wait = WebDriverWait(self.browser, 10)
        return  wait.until(EC.presence_of_element_located(locator))

    def authorization(self, browser):
        """
        Загрузка куков с заранее авторизованным пользователем.
        :param browser: Сетевой драйвер Chrome.
        """
        browser.delete_all_cookies()
        with open('cookies/cookies.json', 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()

    def set_compare(self, browser):
        """
        Загрузка куков с заранее авторизованным пользователем и выбранными телефонами.
        :param browser: Сетевой драйвер Chrome.
        """
        browser.delete_all_cookies()
        with open('cookies/cookies_test_prise_range.json', 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()

    def set_cookie(self, browser):
        """
        Перезаписывает куки, необходимо если onliner изменит список телефонов.
        :param browser: Сетевой драйвер Chrome.
        """
        cookies = browser.get_cookies()
        with open('cookies/cookies_test_prise_range.json', 'w') as file:
            json.dump(cookies, file)
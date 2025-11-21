from contextlib import contextmanager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_by_xpath(self, locator):
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """
        wait = WebDriverWait(self.driver, 10)
        return  wait.until(EC.visibility_of_element_located(locator))

    def find_by_xpath_presence_elem(self, locator):
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """
        wait = WebDriverWait(self.driver, 10)
        return  wait.until(EC.presence_of_element_located(locator))

    def find_by_xpath_clickable_elem(self, locator):
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """

        wait = WebDriverWait(self.driver, 10)
        return  wait.until(EC.element_to_be_clickable(locator))

    @staticmethod
    def authorization(driver, path):
        """
        Загрузка куков с заранее авторизованным пользователем.
        :param driver: Сетевой драйвер Chrome.
        :param path: Путь к кукам для авторизации
        """
        driver.delete_all_cookies()
        with open(path, 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
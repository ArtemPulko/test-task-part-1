from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        """Метод для перехода на страницу по ссылке."""
        self.driver.get(url)

    def scroll_to_element(self, element: WebElement):
        """Прокрутка страницы до указанного элемента
        :param element: WebElement до которого нужно листать страницу
        """
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def find_by_xpath(self, locator: tuple[str, str]) -> WebElement:
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """
        wait = WebDriverWait(self.driver, 10)
        return  wait.until(EC.visibility_of_element_located(locator))

    def find_by_xpath_presence_elem(self, locator: tuple[str, str]) -> WebElement:
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """
        wait = WebDriverWait(self.driver, 10)
        return  wait.until(EC.presence_of_element_located(locator))

    def find_by_xpath_clickable_elem(self, locator: tuple[str, str]) -> WebElement:
        """
        Поиск элемента на странице по XPATH.
        :param locator: Кортеж вида (By.XPATH, XPATH).
        :return: Искомый WebElement.
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        return element





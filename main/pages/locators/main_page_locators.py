from selenium.webdriver.common.by import By
import enum

class MainPageLocators(enum.Enum):

    #XPATH локаторы
    catalog_link = (By.XPATH, '(//a[@class="project-navigation__link project-navigation__link_primary"])[1]')
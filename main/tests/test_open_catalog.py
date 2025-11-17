import pytest

from main.pages.onliner_page import OnlinerPage

@pytest.mark.run(order=1)
def test_mobile_phone_btn(driver):
    """
    Открыть категорию "Мобильные телефоны".
    Убедиться, что она открыта.
    """
    onliner_page = OnlinerPage(driver)
    onliner_page.open()
    #Открываю страницу
    onliner_page.mobile_phone_btn.click()
    #Убедиться, что она открыта.
    assert onliner_page.cotalog_isLoaded

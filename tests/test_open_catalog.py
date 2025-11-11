from Pages.onliner_page import OnlinerPage

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

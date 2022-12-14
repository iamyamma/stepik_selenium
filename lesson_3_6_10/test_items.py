from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(url)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), "no button..."

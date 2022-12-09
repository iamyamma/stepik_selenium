from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from my_defs import equal

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(url)
    WebDriverWait(browser, 12).until(text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, "book").click()
    button = browser.find_element(By.ID, 'solve')
    # browser.execute_script('return arguments[0].scrollIntoView(true)', button)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(equal(x))
    button.click()
    number = browser.switch_to.alert.text.split()[-1]
    print(number)

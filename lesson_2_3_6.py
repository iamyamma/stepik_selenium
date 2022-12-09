from my_defs import equal
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(url)
    # убираем троллфейс
    # sleep(1)
    # browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    # sleep(1)
    browser.find_element(By.TAG_NAME, 'button').click()
    new_tab = browser.window_handles[-1]
    print(new_tab)
    browser.switch_to.window(new_tab)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(equal(x))
    browser.find_element(By.TAG_NAME, 'button').click()
    sleep(5)

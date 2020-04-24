from selenium import webdriver
import math
import pyperclip
import re

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id('input_value').text
    calc_x = calc(x)
    fild_inp = browser.find_element_by_id('answer')
    fild_inp.send_keys(calc_x)

    submit = browser.find_element_by_tag_name('button')
    submit.click()
    text = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    pyperclip.copy(re.search(r'\d*\.\d*', text)[0])
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
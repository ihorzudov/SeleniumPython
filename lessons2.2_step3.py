from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    a = browser.find_element_by_id("num1")
    b = browser.find_element_by_id("num2")

    result = str(int(a.text) + int(b.text))


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)



    button = browser.find_element_by_css_selector ("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
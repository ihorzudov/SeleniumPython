from selenium import webdriver
import time
import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    a = calc(x)


    input1 = browser.find_element_by_id("answer")
    input1.send_keys(a)

    input2=browser.find_element_by_id("robotCheckbox")
    input2.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input3 = browser.find_element_by_id("robotsRule")
    input3.click()

    button = browser.find_element_by_css_selector ("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
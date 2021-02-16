from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = browser.find_element_by_css_selector("span#num1")
    num2 = browser.find_element_by_css_selector("span#num2")
    sum = int(num1.text) + int(num2.text)
    answer = browser.find_element_by_css_selector("#dropdown")
    answer.send_keys(str(sum))
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
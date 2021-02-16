from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element_by_css_selector("#input_value")
    y = calc(int(x.text))
    browser.execute_script("window.scrollBy(0, 225);")
    browser.find_element_by_css_selector("#answer").send_keys(str(y))
    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    browser.find_element_by_css_selector('[for="robotsRule"]').click()
    browser.find_element_by_css_selector("button.btn").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
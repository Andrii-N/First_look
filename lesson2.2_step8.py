from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    info = ['Andrew', 'Gretzki', 'email@e.com']
    selectors = ['[name="firstname"]', '[name="lastname"]', '[name="email"]']
    for x in selectors:
        for i in range(len(info)):
            browser.find_element_by_css_selector(x).send_keys(info[i])
            info.pop(i)
            time.sleep(0.5)
            break
    current = os.path.abspath(os.path.dirname('lesson2.2_step8.py'))
    file_path = os.path.join(current, 'file.txt')
    browser.find_element_by_css_selector('[type = "file"]').send_keys(file_path)
    browser.find_element_by_css_selector("button").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()



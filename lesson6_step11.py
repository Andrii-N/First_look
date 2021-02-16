from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    classlist = [".form-group.first_class>.first:required",
                 ".form-group.second_class>.second:required",
                 ".form-group.third_class>.third:required"]
    for x in classlist:
        element = browser.find_element_by_css_selector(x)
        element.send_keys("Info")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
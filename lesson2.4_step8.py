from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calx(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100"))
browser.find_element_by_css_selector("button#book").click()
x = browser.find_element_by_css_selector("#input_value").text
y = calx(x)
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("button#solve").click()









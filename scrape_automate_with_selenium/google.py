# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

browser = webdriver.Chrome(
    service=ChromiumService(
        ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install()))


url = 'https://duckduckgo.com/'
browser.get(url)
search_el = browser.find_element('name', 'q')
print(search_el)
search_el.send_keys('selenium python')
submit_btn_el = browser.find_element(By.CLASS_NAME, 'search__button')
print(submit_btn_el)
time.sleep(2)
submit_btn_el.click()

time.sleep(5)
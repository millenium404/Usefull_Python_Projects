import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from env import INSTA_USERNAME, INSTA_PASSWORD

browser = webdriver.Chrome(
    service=ChromiumService(
        ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install()))

url = 'https://instagram.com'
browser.get(url)

time.sleep(2)

def find_button_by_name(btn_name, btn_list):
    for button in btn_list:
        if button.text == btn_name:
            return button

buttons = browser.find_elements(By.TAG_NAME, 'button')
allow_cookies_btn = find_button_by_name(
        'Only allow essential cookies', buttons)
login_button = find_button_by_name('Log In', buttons)

allow_cookies_btn.click()
time.sleep(2)

username_el = browser.find_element('name', 'username')
username_el.send_keys(INSTA_USERNAME)
password_el = browser.find_element('name', 'password')
password_el.send_keys(INSTA_PASSWORD)
time.sleep(1)
# login_button.click()


# Wait for 'end' command to exit
command = input('\nType "end" to exit: ')
while command != 'end':
    command = input('\nType "end" to exit: ')
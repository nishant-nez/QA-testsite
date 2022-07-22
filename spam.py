from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import string

chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(service=Service("C:\Program Files\chromedriver.exe"), options=chrome_options)
# driver.get("https://automationintesting.online/")

for i in range(10):
    driver = webdriver.Chrome(service=Service("C:\Program Files\chromedriver.exe"), options=chrome_options)
    driver.get("https://automationintesting.online/")

    sleep(1)
    em = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    em = em + '@gmail.com'
    fnm = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    lnm = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    ph = random.randint(10000000000, 999999999999)
    sub = ''.join(random.choice(string.ascii_letters) for _ in range(11))
    msg = ''.join(random.choice(string.ascii_letters) for _ in range(70))

    name = driver.find_element(by=By.XPATH, value='//*[@id="name"]')
    name.send_keys(fnm + ' ' + lnm)
    email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
    email.send_keys(em)
    phone = driver.find_element(by=By.XPATH, value='//*[@id="phone"]')
    phone.send_keys(ph)
    subject = driver.find_element(by=By.XPATH, value='//*[@id="subject"]')
    subject.send_keys(sub)
    message = driver.find_element(by=By.XPATH, value='//*[@id="description"]')
    message.send_keys(msg)

    submit_btn = driver.find_element(by=By.XPATH, value='//*[@id="submitContact"]')
    submit_btn.click()

    # sleep(5000)
    print(f"pass {i}")
    sleep(3)

driver.close()
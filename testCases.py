from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

datas = [
    {
        'name': 'firstName lastName',
        'email': 'abc@gmail.com',
        'phone': 12345678901,
        'subject': 'Sub Title',
        'message': 'this is test message to send into the test site',
        'expected': True
    },
    {
        'name': 7627345,
        'email': 'abc@gmail.com',
        'phone': 12345678901,
        'subject': 'Sub Title',
        'message': 'this is test message to send into the test site',
        'expected': False
    },
    {
        'name': 'firstName lastName',
        'email': 'abc.com',
        'phone': 12345678901,
        'subject': 'Sub Title',
        'message': 'this is test message to send into the test site',
        'expected': False
    },
    {
        'name': 'firstName lastName',
        'email': 'abc@gmail.com',
        'phone': 12,
        'subject': 'Sub Title',
        'message': 'this is test message to send into the test site',
        'expected': False
    },
    {
        'name': 'firstName lastName',
        'email': 'abc@gmail.com',
        'phone': 12345678901,
        'subject': 'Sub',
        'message': 'this is test message to send into the test site',
        'expected': True
    },
    {
        'name': 'firstName lastName',
        'email': 'abc@gmail.com',
        'phone': 'stringnum',
        'subject': 'Sub Title',
        'message': 'this is test message to send into the test site',
        'expected': False
    },
    {
        'name': 'firstName lastName',
        'email': 'abc',
        'phone': 12345678901,
        'subject': 'Sub Title',
        'message': 'th',
        'expected': False
    },
]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

for data in datas:
    # replace the destination 
    driver = webdriver.Chrome(service=Service("C:\Program Files\chromedriver.exe"), options=chrome_options)
    driver.get("https://automationintesting.online/")

    sleep(2)
    name = driver.find_element(by=By.XPATH, value='//*[@id="name"]')
    name.send_keys(data['name'])
    email = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
    email.send_keys(data['email'])
    phone = driver.find_element(by=By.XPATH, value='//*[@id="phone"]')
    phone.send_keys(data['phone'])
    subject = driver.find_element(by=By.XPATH, value='//*[@id="subject"]')
    subject.send_keys(data['subject'])
    message = driver.find_element(by=By.XPATH, value='//*[@id="description"]')
    message.send_keys(data['message'])

    submit_btn = driver.find_element(by=By.XPATH, value='//*[@id="submitContact"]')
    submit_btn.click()

    sleep(3)

    try:
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div[5]/div[2]/form/div[6]')
        # driver.find_element(by=Class, value='alert-danger')
        # print("\nfound\n")
        obtained = False
    except:
        # print("\nnot found\n")
        obtained = True


    if data['expected'] == obtained:
        print(
            f"Name: {data['name']}, Email: {data['email']}, Phone: {data['phone']}, Subject: {data['subject']}, "
            f"Message: {data['message']}, Expected: {data['expected']}, Obtained: {obtained} | Status: True")
    else:
        print(f"Name: {data['name']}, Email: {data['email']}, Phone: {data['phone']}, Subject: {data['subject']}, "
            f"Message: {data['message']}, Expected: {data['expected']}, Obtained: {obtained} | Status: False")

    driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_service = Service(r"D:\DNC\thuctapthaykhoi\chromedriver-win64\chromedriver.exe")

def connect_to_browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        browser = webdriver.Chrome(service = chrome_service, options=chrome_options)
        try:
            browser.get('https://www.facebook.com')

            email_field = browser.find_element(By.ID, "email")
            email_field.clear()
            for i in id_str:
                email_field.send_keys(i)
                time.sleep(0.3)

            password_field = browser.find_element(By.ID, "pass")
            password_field.clear()
            for p in pass_str:
                password_field.send_keys(p)
                time.sleep(0.2)

            time.sleep(0.5)

            password_next_button = browser.find_element(By.NAME,"login")
            password_next_button.click()

            time.sleep(10)
        except:
            print("heloanhem")

    else:
        print("email hoặc mật khẩu rổng (null)")


connect_to_browser("tthai9123456@gmail.com", "0123456789099")
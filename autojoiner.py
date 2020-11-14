from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import argv 
import time


script, email, password = argv
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get("https://teams.microsoft.com")

def try_locating_element(id):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, id))
        )
    except:
        print("Nie zlokalizowano")
        driver.quit()

try_locating_element("//input[@id='i0116']")
login_form = driver.find_element_by_xpath("//input[@id='i0116']")
login_form.send_keys(email,Keys.RETURN)


try_locating_element("//input[@id='i0118']")
password_form = driver.find_element_by_xpath("//input[@id='i0118']")
password_form.send_keys(password, Keys.RETURN)
# password_form.send_keys(Keys.RETURN)

try_locating_element("//a[@class='use-app-lnk']")
use_web_app = driver.find_element_by_xpath("//a[@class='use-app-lnk']")
use_web_app.send_keys(Keys.RETURN)






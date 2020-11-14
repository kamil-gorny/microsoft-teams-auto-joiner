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




def try_locating_element(xpath):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    except:
        print("Nie zlokalizowano")
        driver.quit()

def fill_and_move_to_the_next_step(driver, xpath, form_info):
    try_locating_element(xpath)
    form = driver.find_element_by_xpath(xpath)
    form.send_keys(form_info, Keys.RETURN)

#fill email field
fill_and_move_to_the_next_step(driver, "//input[@id='i0116']", email)

#fill password field
fill_and_move_to_the_next_step(driver, "//input[@id='i0118']", password)

#use website insted of app
fill_and_move_to_the_next_step(driver, "//a[@class='use-app-lnk']", '')







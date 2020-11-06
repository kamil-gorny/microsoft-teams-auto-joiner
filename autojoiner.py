from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://teams.microsoft.com")


wait  = WebDriverWait(driver, 100).until(EC.title_is('Sign in to your account'))
login_form = driver.find_element_by_id('i0116')
login_form.send_keys("k.gorny.981@studms.ug.edu.pl")

login_button = driver.find_element_by_id('idSIButton9')
login_button.send_keys(Keys.RETURN)


# password_form = driver.find_element_by_id('i0118')
# WebDriverWait(driver, 60).until(EC.find_element_by_id('i0118'))
# WebDriverWait(driver, 60).until(EC.find_element_by_id('idSIButton9'))
# login_button = driver.find_element_by_id('idSIButton9')
# login_button.send_keys(Keys.RETURN)
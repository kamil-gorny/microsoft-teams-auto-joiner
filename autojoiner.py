from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://teams.microsoft.com")




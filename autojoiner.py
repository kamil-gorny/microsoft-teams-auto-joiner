from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
def main():
   driver = webdriver.Chrome(PATH)
  
main()
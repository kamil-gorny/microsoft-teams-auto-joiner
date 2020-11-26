from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import argv 
from datetime import datetime
import time
from consolemenu import * 
from consolemenu.items import *
import json
import threading

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
# options.headless = True 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)


driver.get("https://teams.microsoft.com")
def enter_credentials():
    login = input("Enter login: ")
    password = input("Enter password: ")

    credentials = {"login": login, "password": password}
    f = open('credentials.json', "w")
    f.write(json.dumps(credentials))
    f.close()


def display_menu():
    txt = open('autojoiner.txt', 'r', encoding='utf-8')
    menu = ConsoleMenu(txt.read(), "")
    menu_item = MenuItem("Enter credentials: ")
    function_item = FunctionItem("Scheadule meetings: ", enter_credentials, "")
    menu.append_item(menu_item)
    menu.append_item(function_item)
    menu.show()

def try_locating_element(xpath):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    except:
        print("Nie zlokalizowano")
        # driver.quit()

def fill_and_move_to_the_next_step(driver, xpath, form_info):
    try_locating_element(xpath)
    form = driver.find_element_by_xpath(xpath)
    form.send_keys(form_info, Keys.RETURN)

def get_teams(driver):
    try_locating_element("//div[@class='team-card']")
    teams_elements = driver.find_elements_by_class_name('team-name-text')
    teams = []
    for element in teams_elements:
        teams.append(element.get_attribute('innerHTML'))
    return teams 

menu_thread = threading.Thread(target=display_menu)
menu_thread.start()

fill_and_move_to_the_next_step(driver, "//input[@id='i0116']", "kamil")

#fill password field
fill_and_move_to_the_next_step(driver, "//input[@id='i0118']","pass")

#use website insted of app
# fill_and_move_to_the_next_step(driver, "//a[@class='use-app-lnk']", '')








# input_thread = threading.Thread(target=get_input)
# input_thread.start()

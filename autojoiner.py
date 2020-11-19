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

# script, email, password = argv
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
# options.headless = True 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=PATH)

driver.get("https://teams.microsoft.com")

def display_welcome_screen():
    
    print("---------------------------------------------------------------------------------------------------------------")
    # print(txt.read())
    print("---------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tWitaj w programie Microsoft Teams Auto Joiner")
    print("---------------------------------------------------------------------------------------------------------------")
def enter_credentials():
    
    print("siurek")
    time.sleep(10)
def display_menu():
    txt = open('autojoiner.txt', 'r', encoding='utf-8')
    menu = ConsoleMenu(txt.read(), "")
    menu_item = MenuItem("Wprowadź dane do logowania")
    function_item = FunctionItem("Zaplanuj zajęcia", enter_credentials, "")
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

# display_welcome_screen()
display_menu()
# email = input("Podaj email do platformy: ")
# password = input("Podaj haslo: ")
#fill email field
fill_and_move_to_the_next_step(driver, "//input[@id='i0116']", email)

#fill password field
fill_and_move_to_the_next_step(driver, "//input[@id='i0118']", password)

#use website insted of app
# fill_and_move_to_the_next_step(driver, "//a[@class='use-app-lnk']", '')

for element in get_teams(driver):
    print(element)


# class Team():
#     def __init__(self, team_name, start_time_window):
#         self.team_name = team_name

# team_1 = Team(get_teams(driver)[0])
# print(team_1.team_name)




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from consolemenu import * 
from consolemenu.items import *
from consolemenu.screen import Screen
import json
import threading
import os



PATH = "C:\Program Files (x86)\chromedriver.exe"


def enter_credentials():
    login = input('Enter login: ')
    password = input('Enter password: ')
    credentials = {'login': login, 'password': password}
    with open('credentials.json', 'w') as f:
        f = open('credentials.json', 'w')
        f.write(json.dumps(credentials))

def write_json(data, filename='meetings.json'):
    with open(filename, 'w') as f:
        json.dump(data, f) 


def add_meeting(team):
    with open('meetings.json') as f:
        data = json.load(f)
        temp = data["meetings"]
    for el in temp:
        if el["team_name"] == team:
            print(f"Meeting for {el['team_name']} already exist it is scheduled on {el['day']} at {el['time']} on {el['chanel']} chanel")
            edit_flag = input("What do you want to do with it?(Edit/Remove/Leave)")
            if edit_flag == 'Edit':
                day = input('Enter day of the week: ')
                time = input('Enter meeting start time: ')
                chanel = input('Enter chanel name that meeting take place on: ')
                el["team_name"] = team
                el["day"] = day
                el["time"] = time
                el["chanel"] = chanel 
                write_json(data)
            elif edit_flag == 'Remove':
                temp.remove(el)
                write_json(data)
        else:
            print(f"Enter info for {team}")
            day = input('Enter day of the week: ')
            time = input('Enter meeting start time: ')
            chanel = input('Enter chanel name that meeting take place on: ')
            with open('meetings.json') as f:
                data = json.load(f)
                temp = data["meetings"]
                meeting = {"team_name": team, "day": day, "time": time, "chanel": chanel}
                temp.append(meeting)
            write_json(data)

    
def fill_empty_meetings(team):
    with open('meetings.json', 'a') as f:
        data = {}
        data['meetings'] = []
        f.write(json.dumps(data))

def create_menu_items_for_teams(teams):
    with open('autojoiner.txt', 'r', encoding="utf-8") as txt:
        menu = ConsoleMenu('',txt.read())
        for team in teams:
            menu.append_item(FunctionItem(team, add_meeting, args=[team]))
    return menu
            

def display_main_menu(teams):
    teams_menu = create_menu_items_for_teams(teams)
    with open('autojoiner.txt', 'r', encoding="utf-8") as txt:
        menu = ConsoleMenu('', txt.read())
        menu_item = FunctionItem('Enter credentials ', enter_credentials)
        function_item = SubmenuItem('Scheadule meetings ', teams_menu, menu=menu)
        menu.append_item(menu_item)
        menu.append_item(function_item)
        menu.show()


def try_locating_element(xpath, driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    except:
        print('Nie zlokalizowano')


def fill_and_move_to_the_next_step(driver, xpath, form_info):
    try_locating_element(xpath, driver)
    form = driver.find_element_by_xpath(xpath)
    form.send_keys(form_info, Keys.RETURN)

 
def get_teams(driver):
    try_locating_element("//div[@class='team-card']", driver)
    teams_elements = driver.find_elements_by_class_name('team-name-text')
    teams = []
    for element in teams_elements:
        teams.append(element.get_attribute('innerHTML'))
    return teams


def sign_in(driver):
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
        fill_and_move_to_the_next_step(driver,"//input[@id='i0116']", credentials['login'])
        fill_and_move_to_the_next_step(driver, "//input[@id='i0118']",credentials['password'])
        

def check_for_credentials():
    with open('credentials.json', 'r') as f:
        try:
            credentials = json.load(f)
            if credentials['login'] != '' and credentials['password'] != '':
                return True
            else:
                return False
        except:
            return False


def display_credentials_menu():
    with open('autojoiner.txt', 'r', encoding='utf-8') as txt:
        menu = ConsoleMenu('', txt.read())
        credentials_menu = FunctionItem('Enter credentials', enter_credentials)
        menu.append_item(credentials_menu)
        menu.show()


def start_autojoiner(driver):
    if check_for_credentials():
        driver.get('https://teams.microsoft.com')
        sign_in(driver)
        teams = get_teams(driver)
        menu_thread = threading.Thread(target=display_main_menu(teams))
        menu_thread.start()
    else:
        display_credentials_menu()
        start_autojoiner(driver)


def main():
    options = webdriver.ChromeOptions()
    options.headless = True 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    start_autojoiner(driver)
    time.sleep(1)
 
if __name__ == '__main__':
    main()






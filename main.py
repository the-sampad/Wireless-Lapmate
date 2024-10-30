import undetected_chromedriver as uc
uc.install()

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import os
import subprocess
import pyautogui
import time

from time import sleep
from pywinauto import Application

USERNAME = 'socedu8772@gmail.com'
PASSWORD = 'Socedu%^@2000'

options = Options()
options.add_argument('--headless')

def clear_note_area():
    action = ActionChains(driver)
    action.send_keys('All clear').perform()
    action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
    action.send_keys(Keys.DELETE).perform()

driver = Chrome(options=options)
driver.get("https://app.simplenote.com/")

driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(USERNAME)
print('entered Email')

driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
print('entered Password')

driver.find_element(By.XPATH, '//*[@id="login"]/input[4]').click()
print('clicked Login')

while True:
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/aside/div[3]/div/div[1]/div/div/div[1]/div/button/div/span').text == 'New Note…'
        print('Successfully Logged In')
        sleep(3)
        print('Ready for the Instructions')
        break
    except NoSuchElementException:
        pass

while True:
    instruction = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/main/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[4]/div/span/span').text.lower()
    if instruction != '':
        if ('write' or 'take a note')  in instruction:
            inst = instruction.split('write')
            print(inst)
            # Start Notepad
            subprocess.Popen(['notepad.exe'])

            # Wait for Notepad to start up
            time.sleep(1)

            # Type some text
            pyautogui.typewrite(inst[1])

            clear_note_area()

        elif 'shut down pc' in instruction:
            print('Shutting down in 10s')
            clear_note_area()
            os.system("shutdown /s /t 10")
            break

    sleep(60)
    



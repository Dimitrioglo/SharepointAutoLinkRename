"""
route link renaming automation on Sharepoint
"""

import os
from selenium import webdriver
import autoit
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

import time

# headless mode
# chromeOptions = Options()
# chromeOptions.headless = True
# driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=chromeOptions)
# driver = webdriver.Chrome(executable_path=".\chromedriver.exe", options=chromeOptions)

# unheadless mode

# PATH = ".\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options, executable_path='.\chromedriver.exe')

try:

    linkToRename = "http://repositorydoc.ced.it/portale/documeto/MP/641693/RoutingRules/Raggruppa%20per%20tipo%20di%20contenuto.aspx"
    # # linkToRename = "https://Authorization: Basic aHR0cHdhdGNoOmZmZmY=@www.httpwatch.com/httpgallery/authentication/authenticatedimage/default.aspx"
    driver.get(linkToRename)
    time.sleep(5)

    os.system(r'".\Auth.exe"')

    index = 1
    try:
        # versiunea lucreaza WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//tbody[5]/tr[1]/td[4]'))).click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//tbody[5]/tr[1]/td[4]'))).click()
        time.sleep(1)
        print("Element found")
    except:
        print("Element not found")

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//tbody[5]/tr[1]/td[1]'))).click()
        time.sleep(1)
        print("Element found checkbox")
    except:
        print("Element not found checkbox"
              "")

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "Ribbon.ListItem.Manage.EditProperties-Large"] / span[2]'))).click()
        time.sleep(1)
        print("Element found 1")
    except:
        print("Element not found 1")

    time.sleep(2)


    driver.switch_to.frame(2)
    print("i swithed frame")
    time.sleep(1)
    inputElement = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ctl00_PlaceHolderMain_targetLocationSection_ctl02_pathField_ctl00_TextField')))
    valueElement = driver.find_element_by_xpath('//*[@id="ctl00_PlaceHolderMain_targetLocationSection_ctl02_pathField_ctl00_TextField"]').get_attribute("value")

    newLink = valueElement.replace('/MP2017/', '/MP/')
    newLink = newLink.replace('Conversione Dati', 'Conversione')
    print("new link: " + newLink)

    #delete old value input field
    inputElement.send_keys(Keys.BACK_SPACE)
    inputElement.send_keys(Keys.CONTROL + "a")
    inputElement.send_keys(Keys.DELETE)

    inputElement.send_keys(newLink)

    print("Element found input")

    time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "ctl00_PlaceHolderMain_ctl00_RptControls_buttonOkUpdateRule"]'))).click()
        time.sleep(1)
        print("Element OK BUTTON")
    except:
        print("Element OK BUTTON")





except Exception as e:
    print(e)
    print("Я вышел с ошибкой")
    driver.quit()





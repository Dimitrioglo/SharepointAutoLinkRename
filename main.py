"""
route link renaming automation on Sharepoint
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# unheadless mode
PATH = ".\chromedriver.exe"
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options, executable_path=PATH)

try:
    # Link alla pagina per la modifica dei percorsi
    linkToRename = "http://repositorydoc.ced.it/portale/documeto/MP/641693/RoutingRules/Raggruppa%20per%20tipo%20di%20contenuto.aspx"
    driver.get(linkToRename)
    time.sleep(3)

    # Il file con i dati da utenza
    os.system(r'".\Auth.exe"')

    # Numero dei elementi sul pagina
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="group0"]/td/span')))
        maxValue = driver.find_element_by_xpath('//*[@id="group0"]/td/span').text
        maxValueInt = int(maxValue.replace('(', '').replace(')', '').strip())
        time.sleep(1)
    except:
        print("Errore non e stato trovato numero max dei elementi!")

    # Index per iterazione sugli elementi
    index = 1
    while index <= maxValueInt:

        # Elemento CheckBox
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//tbody[5]/tr[' + str(index) + ']/td[1]')))

            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//tbody[5]/tr[' + str(index) + ']/td[1]'))).click()
        except:
            print("Errore su click CheckBox dal elemento!")
            break

        # Bottone Modifica elemento
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, '// *[ @ id = "Ribbon.ListItem.Manage.EditProperties-Large"] / span[2]'))).click()
            time.sleep(2)
        except:
            print("Errore su click Bottone Modifica elemento!")
            break

        # Gestione elemento iframe
        try:
            WebDriverWait(driver, timeout=20).until(EC.frame_to_be_available_and_switch_to_it(2))
        except:
            print("Non e stato trovato elemento iframe!")
            break

        time.sleep(1)

        # Elemento input
        try:
            # Сercare un campo di input che contenga un campo per modificare il percorso
            inputElement = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#ctl00_PlaceHolderMain_targetLocationSection_ctl02_pathField_ctl00_TextField')))

            # Salvare del valore del campo
            valueElement = driver.find_element_by_xpath(
                '//*[@id="ctl00_PlaceHolderMain_targetLocationSection_ctl02_pathField_ctl00_TextField"]').get_attribute(
                "value")

            # Replace i valori di percorso
            newLink = valueElement.replace('/MP2017/', '/MP/')
            # Replace opzione aggiuntiva
            newLink = newLink.replace('Conversione Dati', 'Conversione')

            # cancellando il vecchio valore del campo di input e assegnandone uno nuovo
            inputElement.send_keys(Keys.BACK_SPACE)
            inputElement.send_keys(Keys.CONTROL + "a")
            inputElement.send_keys(Keys.DELETE)
            inputElement.send_keys(newLink)
            time.sleep(2)
        except:
            print("Errore su campo di input text!")
            break

        # Modifica regola - bottone OK
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '// *[ @ id = "ctl00_PlaceHolderMain_ctl00_RptControls_buttonOkUpdateRule"]'))).click()
            time.sleep(1)
        except:
            print("Errore su click bottone OK da Modifica regola!")
            break

        print("Elemento " + str(index) + " di " + str(maxValueInt) + " modificato ")
        index += 1

    if index > maxValueInt:
        print("Il programma è terminato elaborazione. Controlla sul sito web se tutto ha funzionato correttamente")

    # driver.quit()

except Exception as e:
    print("Il programma è terminato con un errore: " + str(e))
    driver.quit()

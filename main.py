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
    linkToRename = "http://repositorydoc.ced.it/portale/documeto/PS/651172/RoutingRules/Raggruppa%20per%20tipo%20di" \
                   "%20contenuto.aspx "
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
        print("Errore non e trovato numero max dei elementi!")

    # Index per iterazione sugli elementi
    index = 1
    while index <= maxValueInt:

        # Rimuovere il commento se il primo elemento Checkbox di controllo non funziona
        # if index == 1:
        #     #Click link area "Percorso di destinazione"
        #     try:
        #         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//tbody[5]/tr[' + str(index) + ']/td[4]'))).click()
        #         time.sleep(1)
        #     except:
        #         print("Errore click su link area Percorso di destinazione!")

        # Elemento CheckBox
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//tbody[5]/tr[' + str(index) + ']/td[1]'))).click()
            time.sleep(1)
        except:
            print("Errore su click CheckBox dal elemento!")
            break

        # Bottone Modifica elemento
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '// *[ @ id = "Ribbon.ListItem.Manage.EditProperties-Large"] / span[2]'))).click()
            time.sleep(2)
        except:
            print("Errore su click Bottone Modifica elemento!")
            break

        time.sleep(5)


        def frame_available_check(frame_reference):
            """Verifica se elemento iframe esiste nella pagina ciclo ricorsivo."""

            def callback(driver):
                try:
                    driver.switch_to.frame(frame_reference)
                except NoSuchFrameException:
                    return False
                else:
                    return True

            return callback


        # Gestione elemento iframe
        try:
            WebDriverWait(driver, timeout=20).until(frame_available_check(2))
        except:
            print("Non e trovato elemento iframe!")
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
            newLink = valueElement.replace('/PS2017/', '/PS/')
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

    if index == maxValueInt:
        print("Il programma è terminato elaborazione. Controlla sul sito web se tutto ha funzionato correttamente")

    driver.quit()

except Exception as e:
    print("Il programma è terminato con un errore: " + str(e))
    driver.quit()

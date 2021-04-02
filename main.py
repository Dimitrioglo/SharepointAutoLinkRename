# Nedobot game automatization

from selenium import webdriver
import random
import telegram_send
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# headless mode
chromeOptions = Options()
chromeOptions.headless = True
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=chromeOptions)

# unheadless mode
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
try:
    driver.get("https://vk.com/im?sel=c105")
    element = driver.find_element_by_id("email")
    element.send_keys("37360978889")

    element = driver.find_element_by_id("pass")
    element.send_keys("Google24")
    print(driver.title)

    element = driver.find_element_by_class_name("login_button")
    element.click()

    driver.implicitly_wait(5)

    driver.find_element_by_css_selector("#l_msg > a > span.left_label.inl_bl").click()

    driver.find_element_by_css_selector("#im_dialogs > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > li.nim-dialog._im_dialog._im_dialog_2000000105.nim-dialog_muted > div.nim-dialog--content > div").click()

    def presentCapthcha():
        driver.implicitly_wait(30)
        list_of_elements = driver.find_element_by_css_selector("div.im-page--chat-body").text
        time.sleep(1)
        if list_of_elements.find('Funeral , наша система заподозрила автоматизацию') != -1:
            # timeOfCapthcha = driver.find_element_by_class_name('_im_mess_link').text
            # print("time capthcha: " + str(timeOfCapthcha))
            telegram_send.send(messages=["Ooops...you have to enter captcha ^_^ "])
            while True:
                try:
                    list_of_elements = driver.find_element_by_css_selector("div.im-page--chat-body").text
                    if list_of_elements.find('Funeral , капча решена. Блокировка заработков снята') != -1:
                    #timeSolved = driver.find_element_by_class_name('_im_mess_link').text
                    # print("timeSolved: " + str(timeSolved))
                        break
                    else:
                        time.sleep(5)
                except:
                    time.sleep(5)

    while True:
        # Fishing
        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(2) > div:nth-child(1) > button"))).click()
            time.sleep(1)
        except:
            telegram_send.send(messages=["Кнопка рыбалка не сработала"])

        # Mine
        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(2) > div:nth-child(2) > button"))).click()
            time.sleep(1)
        except:
            telegram_send.send(messages=["Кнопка шахта не сработала"])

        # Hunter
        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(2) > div:nth-child(3) > button"))).click()
            time.sleep(1)
        except:
            telegram_send.send(messages=["Кнопка охота не сработала"])

        #collect water
        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(3) > div:nth-child(1) > button"))).click()
            time.sleep(1)
        except:
            telegram_send.send(messages=["Кнопка сбора воды не сработала"])

        #polivka
        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(3) > div:nth-child(2) > button"))).click()
            time.sleep(1)
        except:
            telegram_send.send(messages=["Кнопка полива не сработала"])

        #Urojay
        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="_im_keyboard_container"]/div/div/div[1]/div[1]/div/div[1]/div/div[3]/div[3]/button'))).click()
            time.sleep(1)
        except:
            print("урожай не сработал")

        presentCapthcha()
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="_im_keyboard_container"]/div/div/div[1]/div[1]/div/div[1]/div/div[3]/div[4]/button'))).click()
            time.sleep(1)
        except:
            print("кормежка не сработала")


        i = 0
        while i < 10:

            myTimeValue = random.randrange(61, 72)

            print("Next work after: " + str(myTimeValue) + " seconds")
            time.sleep(myTimeValue)

            i += 1
            presentCapthcha()
            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(1) > div:nth-child(1) > button"))).click()
                driver.implicitly_wait(50)
                time.sleep(1)
            except:
                telegram_send.send(messages=["Кнопка работы не сработала"])

            presentCapthcha()

            if 0 == i % 2:
                try:
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#_im_keyboard_container > div > div > div.ui_scroll_overflow > div.ui_scroll_outer > div > div.ui_scroll_content.clear_fix > div > div:nth-child(1) > div:nth-child(2) > button"))).click()
                except:
                    telegram_send.send(messages=["Кнопка гонки не сработала"])

            print("For full farm remained " + str(i) + " of 10 works")
except:
    print("Я вышел с ошибкой")
    driver.quit()





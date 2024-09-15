from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://www.delta.com')

check_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link-check-in"))
)
check_in_button.click()
confirmation_field = driver.find_element(By.ID, 'confirmationNumber')  
confirmation_field.send_keys(confirmation_code)
from_airport_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "departureAirportLink"))
)
from_airport_link.click()

from_airport_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "search_input"))
)
from_airport_input.send_keys("BOS")

try:
    first_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//li[contains(., 'Boston, MA')])[1]")) 
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", first_option)
    first_option.click()
except Exception as e:
    print(f"Error selecting airport option: {e}")
    driver.quit()
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.ESCAPE)
try:
    nextCheckIn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn-checkin-submit"))
    )
    nextCheckIn.click()
except Exception as e:
    print(f"Error clicking Next button: {e}")
    driver.quit()

time.sleep(3)  

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-primary btn-block btn-shadow-on-focus'])[1]"))
)
next_button.click()

complete_checkin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary btn-block btn-shadow-on-focus' and contains(text(), 'COMPLETE CHECK IN')]"))
    )    
complete_checkin_button.click()

try:
    done_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary btn-block btn-shadow-on-focus' and contains(text(), 'DONE')]"))
    )
    done_button.click()
except Exception as e:
    print(f"Error clicking the DONE button: {e}")
    driver.quit()

time.sleep(10)  
driver.quit()
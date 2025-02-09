import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkboxes = driver.find_elements(By.XPATH,"//input[@type= 'checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_checkboxes = 3

if expected_checkboxes == checked_count:
    print("Check box count verified")
else :
    print("checkbox count mismatch")

time.sleep(5)
driver.close()
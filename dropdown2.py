# Interact with Dropdown
#Check whether the target option is available

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

dropdown = driver.find_element(By.ID,"dropdown-class-example")
select = Select(dropdown)

target_value = "Option3"

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option {target_value} not found")


time.sleep(3)
# Interact with Dropdown

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

dropdown = driver.find_element(By.ID,"dropdown-class-example")
select = Select(dropdown)

#Select one option
    #Select the value by the visible text
    #Select the value by index
    #Select the option by using a value

    #select.select_by_visible_text("Option2")
    #select.select_by_index(2)
    #select.select_by_value("option2")

#Count the options values
option_count = len(select.options)
expected_count = 4

if option_count == expected_count:
    print("Test case passed. Count is correct")
else:
    print("Test case failed. Count is incorrect")

time.sleep(3)
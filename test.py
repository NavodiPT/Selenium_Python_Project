from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time

from log import success_element

# Open Chrome browser
driver = webdriver.Chrome()

# Open W3Schools
driver.get("https://www.w3schools.com/")
driver.maximize_window()
title = driver.title
print(title)

assert "Web" in title

#Search bar operation
search_bar = driver.find_element(By.XPATH,"//input[@id='search2']")
assert not search_bar.get_attribute("disabled")
search_bar.click()
time.sleep(2)
search_bar.send_keys("HTML")
time.sleep(2)
search_bar.send_keys(Keys.RETURN)

#click start button
start_btn = driver.find_element(By.XPATH,"//a[normalize-space()='Start learning HTML now »']")
actions = ActionChains(driver)
actions.move_to_element(start_btn).perform()
assert not start_btn.get_attribute("disabled")
start_btn.click()

success_ele = driver.find_element(By.XPATH," //h2[normalize-space()='What is HTML?']")
assert success_ele.text == "What is HTML?"
time.sleep(2)

# Close the browser
driver.quit()




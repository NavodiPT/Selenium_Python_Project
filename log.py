from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

user_name = "standard_user"
password = "secret_sauce"
login_link = "https://www.saucedemo.com/"
driver.get(login_link)

username_field = driver.find_element(By.ID,"user-name")
password_field = driver.find_element(By.ID,"password")
username_field.send_keys(user_name)
password_field.send_keys(password)
time.sleep(2)

submit_btn = driver.find_element(By.ID, "login-button")
assert not submit_btn.get_attribute("disabled")
submit_btn.click()
time.sleep(2)
success_element = driver.find_element(By.CSS_SELECTOR,".title")
assert success_element.text == "Products"

time.sleep(2)
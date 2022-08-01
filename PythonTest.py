
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome("/Users/marijanavukovic/Desktop/SeleniumTest/chromedriver 2")
driver.get("https://staging-ecatch-dashboard.mndnw.sh/sign-in")
driver.maximize_window()
print(driver.title)

username = "marisskg@yahoo.com"
password = "Mara1991!"
driver.find_element(By.NAME, "email").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)

driver.find_element(By.CLASS_NAME, "sc-jomqDZ.jJhmDe").click()

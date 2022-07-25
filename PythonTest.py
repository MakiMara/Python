import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service=Service ("/Users/marijanavukovic/Desktop/SeleniumTest/chromedriver 3")
driver=webdriver.Chrome(service=service)
driver.get("https://staging-ecatch-dashboard.mndnw.sh/sign-in")


time.sleep(5)
Email = driver.find_element(By.NAME, "name")
Email.send_keys("Marijana@mindnow.io")
Pass = driver.find_element(By.NAME, "password")
Pass.send_keys("Mara1991!")


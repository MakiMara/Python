import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DemoFindElementByName():
      def locate_by_name(self) :
          driver=webdriver.Chrome("/Users/marijanavukovic/Desktop/SeleniumTest/chromedriver 2")
          driver.get("https://staging-ecatch-dashboard.mndnw.sh/sign-in")
          driver.maximize_window()
          print(driver.title)
          driver.find_element(By.NAME, "email").send_keys("marisskg@yahoo.com")
          driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Mara1991!")
          driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
          time.sleep(4)
          driver.find_element(By.CLASS_NAME, "Button_root__2VmrF.Button_is-immo__1-wCH.Button_is-small__13zuY").click()

findbyname = DemoFindElementByName()
findbyname.locate_by_name()
